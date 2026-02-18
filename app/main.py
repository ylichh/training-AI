import os

from semantic_kernel_service.semantic_kernel_service import SemanticKernelService
from semantic_kernel_service.connectors import ConnectorFactory
from plugins.weather_plugin import WeatherPlugin
from plugins.email_plugin import EmailPlugin
from email_service.email_sender import EmailSender
from fastapi_controller.fastapi_controller import FastApiController

ai_connector = os.environ.get("AI_CONNECTOR", "ollama")
fastapi_host = os.environ.get("FASTAPI_HOST", "")
fastapi_port = int(os.environ.get("FASTAPI_PORT", ""))

connector_configs = {
    "ollama": {
        "service_id": "ollama",
        "model_id": os.environ.get("OLLAMA_MODEL", ""),
        "host": os.environ.get("OLLAMA_HOST", ""),
    },
    "openai": {
        "service_id": "openai",
        "model_id": os.environ.get("OPENAI_MODEL", ""),
        "api_key": os.environ.get("OPENAI_API_KEY", ""),
        "org_id": os.environ.get("OPENAI_ORG_ID", None),
    },
}

print(f"Usando conector AI: {ai_connector}")
print(f"Configuración del conector: {connector_configs[ai_connector]}")

connector = ConnectorFactory.create(ai_connector, **connector_configs[ai_connector])

sk_service = SemanticKernelService(connector=connector)

EmailPlugin(email_sender=EmailSender(
    user=os.environ.get("SERVICE_MAIL",""),
    password=os.environ.get("SERVICE_PASSWORD","")
))
sk_service.add_plugin(WeatherPlugin(), "weather")

controller = FastApiController(
    sk_service=sk_service,
    host=fastapi_host,
    port=fastapi_port,
)
controller.run()
