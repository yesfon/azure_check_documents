# Azure OpenAI Document Search Service

Este proyecto permite consumir documentos (PDFs, imágenes) y un JSON de consultas desde una carpeta local o un servicio remoto, subirlos a Azure OpenAI Assistants, y obtener fragmentos relevantes como respuesta para cada consulta.

## Estructura

```
check_documents/
├── main.py
├── config.py
├── azure_openai_helper.py
├── requirements.txt
├── .env.example
├── README.md
└── data/
    ├── ejemplo.json
    └── (tus PDFs e imágenes)
```

## Uso rápido

1. **Clona el repositorio:**
   ```bash
   git clone <TU_REPO_URL>
   cd check_documents
   ```

2. **Copia y edita el archivo de variables de entorno:**
   ```bash
   cp .env.example .env
   # Edita .env con tus credenciales de Azure OpenAI
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Agrega tus documentos y queries:**
   - Coloca tus PDFs, imágenes y un archivo JSON con las consultas en la carpeta `data/`.

5. **Ejecuta el script principal:**
   ```bash
   python main.py
   ```

6. **Resultados:**
   - El archivo `output.json` contendrá las respuestas a tus queries.

## Variables de entorno (`.env`)

```
AZURE_OPENAI_API_KEY=TU_API_KEY_AQUI
AZURE_OPENAI_ENDPOINT=https://TU_ENDPOINT.openai.azure.com/
AZURE_OPENAI_ASSISTANT_ID=TU_ASSISTANT_ID
SOURCE_TYPE=local
SOURCE_PATH=./data
```

No subas tu `.env` real al repositorio, usa `.env.example` como plantilla.

## Notas
- El código está completamente tipado y preparado para pruebas locales y despliegue en otros equipos.
- Si quieres usar un servicio remoto, adapta la función `load_documents_and_queries` en `main.py`.
- El asistente de Azure OpenAI debe estar configurado para aceptar archivos y responder a consultas contextuales.

---

¡Contribuciones y mejoras son bienvenidas!
