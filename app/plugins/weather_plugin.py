from semantic_kernel.functions.kernel_function_decorator import kernel_function


class WeatherPlugin:
    @kernel_function(name="get_weather", description="Gets the current weather for a given city")
    def get_weather(self, city: str) -> str:
        fake_weather = {
            "madrid": "Soleado, 1°C",
            "barcelona": "Nublado, 18°C",
            "londres": "Lluvia, 12°C",
            "nueva york": "Parcialmente nublado, 22°C",
        }
        return fake_weather.get(city.lower(), f"No tengo datos del tiempo para {city}")
