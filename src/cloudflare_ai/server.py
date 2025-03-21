"""Main MCP server implementation."""
from typing import Dict, List
from PIL import Image

from .utils.cloudflare import CloudflareClient
from .tools.generate_images import ImageGenerator, AIModel, ImageSize
from .tools.generate_prompt import PromptGenerator

class ImageGenerationServer:
    def __init__(self, account_id: str = None, api_token: str = None):
        self.client = CloudflareClient(account_id, api_token)
        self.image_generator = ImageGenerator(self.client)
        self.prompt_generator = PromptGenerator(self.client)
    
    def get_models(self) -> List[AIModel]:
        return self.image_generator.get_models()
    
    def get_sizes(self) -> List[ImageSize]:
        return self.image_generator.get_sizes()
    
    def get_themes(self) -> List[str]:
        return self.prompt_generator.get_themes()
    
    async def generate_images(self, prompt: str, size_id: str) -> Dict[str, Image.Image]:
        return await self.image_generator.generate_images(prompt, size_id)
    
    async def generate_prompt(self, theme: str) -> str:
        return await self.prompt_generator.generate_prompt(theme) 