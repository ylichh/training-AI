from semantic_kernel_service.connectors.base_connector import BaseConnector
from semantic_kernel_service.connectors.ollama_connector import OllamaConnector
from semantic_kernel_service.connectors.openai_connector import OpenAIConnector


class ConnectorFactory:
    _connectors = {
        "ollama": OllamaConnector,
        "openai": OpenAIConnector,
    }

    @staticmethod
    def create(connector_type: str, **kwargs) -> BaseConnector:
        connector_class = ConnectorFactory._connectors.get(connector_type)
        if connector_class is None:
            available = ", ".join(ConnectorFactory._connectors.keys())
            raise ValueError(
                f"Conector '{connector_type}' no soportado. Opciones disponibles: {available}"
            )
        return connector_class(**kwargs)
