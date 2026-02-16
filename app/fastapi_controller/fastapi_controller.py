import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from semantic_kernel_service.semantic_kernel_service import SemanticKernelService
from fastapi.middleware.cors import CORSMiddleware

class PreguntaRequest(BaseModel):
    question: str
    context: str


class FastApiController:
    def __init__(self, sk_service: SemanticKernelService, host: str, port: int):
        self.host = host
        self.port = port
        self.app = FastAPI()
        self.app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
        self._register_routes(sk_service)

    def _register_routes(self, sk_service: SemanticKernelService):
        @self.app.post("/pregunta")
        async def pregunta(request: PreguntaRequest):
            print("Pregunta recibida")
            respuesta = await sk_service.ask(request.question, request.context)
            return {"respuesta": respuesta}

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
