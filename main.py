import os
import json
from typing import List, Tuple, Dict, Any
from azure_openai_helper import AzureOpenAIAssistant
from config import Config

def load_documents_and_queries(source_type: str, source_path: str) -> Tuple[List[str], List[str]]:
    """
    Carga documentos y el JSON de queries desde una carpeta local o desde una URL remota.
    """
    files: List[str] = []
    queries: List[str] = []
    if source_type == 'local':
        # Asume que en source_path están los archivos y el JSON
        for file in os.listdir(source_path):
            if file.endswith('.json'):
                with open(os.path.join(source_path, file), 'r', encoding='utf-8') as f:
                    queries = json.load(f)
            else:
                files.append(os.path.join(source_path, file))
        return files, queries
    else:
        # Aquí se podría implementar la descarga remota
        raise NotImplementedError("Sólo implementado para pruebas locales por ahora.")

def main() -> None:
    # Configuración
    config: Config = Config()
    source_type: str = config.SOURCE_TYPE  # 'local' o 'remote'
    source_path: str = config.SOURCE_PATH  # Ruta local o URL

    # Cargar documentos y queries
    files: List[str]
    queries: List[str]
    files, queries = load_documents_and_queries(source_type, source_path)

    # Inicializar asistente de Azure OpenAI
    assistant: AzureOpenAIAssistant = AzureOpenAIAssistant(config)
    assistant.upload_files(files)

    results: List[Dict[str, Any]] = []
    for query in queries:
        fragment: str = assistant.find_relevant_fragment(query)
        results.append({
            'query': query,
            'fragment': fragment
        })

    # Guardar resultados
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Resultados guardados en output.json")

if __name__ == "__main__":
    main()
