from abc import ABC, abstractmethod


class BaseConnector(ABC):
    @abstractmethod
    def create_service(self):
        """Retorna una instancia de chat completion para Semantic Kernel."""
        pass

    @property
    @abstractmethod
    def service_id(self) -> str:
        pass
