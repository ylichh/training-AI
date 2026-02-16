from fastapi import FastAPI
from pydantic import BaseModel

from app.semantic_kernel_service.semantic_kernel_service import SemanticKernelService
from app.plugins.weather_plugin import WeatherPlugin

app = FastAPI()

sk_service = SemanticKernelService(
    service_id="qwen",
    model_id="qwen2.5:3b",
    host="http://localhost:11434",
)
sk_service.add_plugin(WeatherPlugin(), name="weather")


class PreguntaRequest(BaseModel):
    pregunta: str


@app.post("/pregunta")
async def pregunta(request: PreguntaRequest):
    respuesta = await sk_service.ask(request.pregunta)
    return {"respuesta": respuesta}
