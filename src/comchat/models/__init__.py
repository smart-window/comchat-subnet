from .openai import OpenAI
from .openrouter import OpenRouter
from .anthropic import Anthropic
from .togetherai import TogetherAI
from .mistralai import MistralAI
from .groq import Groq
from .perplexity import Perplexity
from .gemini import Gemini

services = {
    'openai': OpenAI,
    'openrouter': OpenRouter,
    'anthropic': Anthropic,
    'togetherai': TogetherAI,
    'mistralai': MistralAI,
    'groq': Groq,
    'perplexity': Perplexity,
    'gemini': Gemini,
}

def get_service_class(service_name):
    return services.get(service_name)