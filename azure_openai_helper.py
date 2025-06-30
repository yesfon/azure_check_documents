import openai
import time
from typing import List, Any
from config import Config

class AzureOpenAIAssistant:
    def __init__(self, config: Config) -> None:
        openai.api_key = config.AZURE_OPENAI_API_KEY
        openai.api_base = config.AZURE_OPENAI_ENDPOINT
        self.assistant_id: str = config.AZURE_OPENAI_ASSISTANT_ID
        self.uploaded_file_ids: List[str] = []

    def upload_files(self, file_paths: List[str]) -> None:
        """
        Sube archivos a Azure OpenAI y guarda los IDs.
        """
        self.uploaded_file_ids = []
        for file_path in file_paths:
            with open(file_path, "rb") as f:
                response: Any = openai.files.create(file=f, purpose="assistants")
                self.uploaded_file_ids.append(response.id)

    def find_relevant_fragment(self, query: str) -> str:
        """
        Crea un thread, adjunta archivos y consulta al asistente.
        Devuelve el fragmento relevante de la respuesta.
        """
        # 1. Crear un thread
        thread: Any = openai.beta.threads.create()
        thread_id: str = thread.id

        # 2. Adjuntar archivos al thread
        for file_id in self.uploaded_file_ids:
            openai.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=f"[Archivo adjunto]",
                file_ids=[file_id]
            )

        # 3. Enviar el mensaje de consulta
        message: Any = openai.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=query
        )

        # 4. Lanzar el run (invoca el asistente sobre el thread)
        run: Any = openai.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=self.assistant_id
        )

        # 5. Esperar a que termine el run
        while True:
            run_status: Any = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status in ["completed", "failed", "cancelled"]:
                break
            time.sleep(2)

        if run_status.status != "completed":
            return f"Error: Run status {run_status.status}"

        # 6. Obtener la respuesta
        messages: Any = openai.beta.threads.messages.list(thread_id=thread_id)
        for msg in reversed(messages.data):
            if msg.role == "assistant":
                return msg.content[0].text.value.strip()
        return "No se encontró respuesta del asistente."
