from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

from semantic_kernel_service.connectors.base_connector import BaseConnector


class OpenAIConnector(BaseConnector):
    def __init__(self, service_id: str, model_id: str, api_key: str, org_id: str | None = None):
        self._service_id = service_id
        self._model_id = model_id
        self._api_key = api_key
        self._org_id = org_id

    @property
    def service_id(self) -> str:
        return self._service_id

    def create_service(self) -> OpenAIChatCompletion:
        return OpenAIChatCompletion(
            service_id=self._service_id,
            ai_model_id=self._model_id,
            api_key=self._api_key,
            org_id=self._org_id,
        )
