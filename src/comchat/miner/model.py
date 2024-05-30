from communex.module import Module, endpoint
from communex.key import generate_keypair
from keylimiter import TokenBucketLimiter
from fastapi import HTTPException
from comchat.models import get_service_class

class Miner(Module):
    """
    A module class for mining and generating responses to prompts.

    Attributes:
        None

    Methods:
        generate: Generates a response to a given prompt using a specified model.
    """
    @endpoint
    def generate(self, service: str, model: str, prompt: str):
        """
        Generates a response to a given prompt using a specified model.

        Args:
            service: The service to use for generating the response. (ex: openai, anthropic ...)
            model: The model to use for generating the response.
            prompt: The prompt to generate a response for.

        Returns:
            None
        """
        print(f"🟡 Service: {service}, Model: {model}")

        if not service or not model or not prompt:
            raise HTTPException(status_code=400, detail=f"Invalid input")

        service_class = get_service_class(service)
        if not service_class:
            raise HTTPException(status_code=400, detail=f"Service not supported")

        service_instance = service_class(model)
        response = service_instance.generate(prompt)
        print(f"🟢 Answer: {response}")

        result = {}
        result["answer"] = response

        return result

if __name__ == "__main__":
    """
    Example
    """
    from communex.module.server import ModuleServer
    import uvicorn
    
    key = generate_keypair()
    miner = Miner()
    refill_rate = 1 / 400
    # Implementing custom limit
    bucket = TokenBucketLimiter(2, refill_rate)
    server = ModuleServer(miner, key, ip_limiter=bucket, subnets_whitelist=[3])
    app = server.get_fastapi_app()

    # Only allow local connections
    uvicorn.run(app, host="127.0.0.1", port=8000)
