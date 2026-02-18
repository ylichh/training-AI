from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

from semantic_kernel_service.connectors.base_connector import BaseConnector


class OllamaConnector(BaseConnector):
    def __init__(self, service_id: str, model_id: str, host: str):
        self._service_id = service_id
        self._model_id = model_id
        self._host = host

    @property
    def service_id(self) -> str:
        return self._service_id

    def create_service(self) -> OllamaChatCompletion:
        return OllamaChatCompletion(
            service_id=self._service_id,
            ai_model_id=self._model_id,
            host=self._host,
        )
