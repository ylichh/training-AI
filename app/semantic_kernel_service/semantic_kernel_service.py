from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory

prompt_template="""Responde la pregunta del usuario basandote en el contexto: {pregunta}
Contexto: {contexto}"""
class SemanticKernelService:
    def __init__(self, service_id: str, model_id: str, host: str, system_prompt: str = "", prompt_template: str = prompt_template):
        self.service_id = service_id
        self.system_prompt = system_prompt
        self.prompt_template = prompt_template
        self.kernel = Kernel()
        self.kernel.add_service(
            OllamaChatCompletion(
                service_id=service_id,
                ai_model_id=model_id,
                host=host,
                
            )
        )

    def add_plugin(self, plugin, name: str):
        self.kernel.add_plugin(plugin, plugin_name=name)

    async def ask(self, question: str, contexto:str) -> str:
        settings = self.kernel.get_prompt_execution_settings_from_service_id(self.service_id)
        settings.options = {
            "temperature": 0.1,
            "top_p": 0.6,
            "num_predict": 300,
        }
        settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

        chat_history = ChatHistory()

        if self.system_prompt:
            chat_history.add_system_message(self.system_prompt)

        user_message = self.prompt_template.format(
            pregunta=question,
            contexto=contexto,
        )
        print(user_message)
        chat_history.add_user_message(user_message)

        response = await self.kernel.get_service(self.service_id).get_chat_message_content(
            chat_history=chat_history,
            settings=settings,
            kernel=self.kernel,
        )
        print(response)
        return str(response)
