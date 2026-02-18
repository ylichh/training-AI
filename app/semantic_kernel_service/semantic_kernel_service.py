from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.functions import KernelFunction

from semantic_kernel_service.connectors.base_connector import BaseConnector

prompt_template="""Responde la pregunta del usuario basandote en el contexto: {{$pregunta}}
Contexto: {{$contexto}}"""
class SemanticKernelService:
    def __init__(self, connector: BaseConnector, system_prompt: str = "", prompt_template: str = prompt_template):
        self.service_id = connector.service_id
        self.system_prompt = system_prompt
        self.prompt_template = prompt_template
        self.kernel = Kernel()
        self.kernel.add_service(connector.create_service())

    def add_plugin(self, plugin, name: str):
        self.kernel.add_plugin(plugin, plugin_name=name)

    async def ask(self, question: str, contexto: str) -> str:
        settings = self.kernel.get_prompt_execution_settings_from_service_id(self.service_id)
        settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
        settings.temperature = 0.7

        ask_function = KernelFunction.from_prompt(
            prompt=self.prompt_template,
            function_name="ask",
            plugin_name="chat",
            prompt_execution_settings={self.service_id: settings},
        )

        response = await self.kernel.invoke(
            ask_function,
            pregunta=question,
            contexto=contexto,
        )
        return str(response)
