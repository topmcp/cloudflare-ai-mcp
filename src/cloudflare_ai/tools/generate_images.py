"""Image generation tools."""
from typing import Dict, Any, List
from dataclasses import dataclass
from PIL import Image

from ..utils.cloudflare import CloudflareClient

@dataclass
class ImageSize:
    id: str
    name: str

@dataclass
class AIModel:
    id: str
    name: str
    description: str
    steps: int = None

class ImageGenerator:
    def __init__(self, client: CloudflareClient):
        self.client = client
        self.models = [
            AIModel("@cf/stabilityai/stable-diffusion-xl-base-1.0", "SDXL Base", "最高质量的SDXL基础版本"),
            AIModel("@cf/bytedance/stable-diffusion-xl-lightning", "SDXL Lightning", "字节优化的快速SDXL版本"),
            AIModel("@cf/lykon/dreamshaper-8-lcm", "Dreamshaper", "快速的Dreamshaper模型", 8),
            AIModel("@cf/black-forest-labs/flux-1-schnell", "Flux Schnell", "轻量快速生成模型", 8)
        ]
        
        self.sizes = [
            ImageSize("1024x1024", "1:1 方形 (1024x1024)"),
            ImageSize("1024x576", "16:9 横向 (1024x576)"),
            ImageSize("576x1024", "9:16 纵向 (576x1024)")
        ]

    async def generate_images(self, prompt: str, size_id: str) -> Dict[str, Image.Image]:
        """使用所有模型生成图像"""
        width, height = map(int, size_id.split('x'))
        tasks = []
        
        for model in self.models:
            task = self.client.generate_image(
                model.id,
                prompt,
                width,
                height,
                model.steps
            )
            tasks.append((model.id, task))
        
        results = {}
        for model_id, task in tasks:
            try:
                image = await task
                results[model_id] = image
            except Exception as e:
                results[model_id] = e
                
        return results

    def get_models(self) -> List[AIModel]:
        """获取所有可用的模型"""
        return self.models

    def get_sizes(self) -> List[ImageSize]:
        """获取所有支持的图像尺寸"""
        return self.sizes 