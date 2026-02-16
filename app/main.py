import os

from semantic_kernel_service.semantic_kernel_service import SemanticKernelService
from plugins.weather_plugin import WeatherPlugin
from plugins.email_plugin import EmailPlugin
from email_service.email_sender import EmailSender
from fastapi_controller.fastapi_controller import FastApiController

ollama_host = os.environ.get("OLLAMA_HOST", "")
ollama_model = os.environ.get("OLLAMA_MODEL", "")
fastapi_host = os.environ.get("FASTAPI_HOST", "")
fastapi_port = int(os.environ.get("FASTAPI_PORT", ""))

sk_service = SemanticKernelService(
    service_id="ollama",
    model_id=ollama_model,
    host=ollama_host,
)
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
