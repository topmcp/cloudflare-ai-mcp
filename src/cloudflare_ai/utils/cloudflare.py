"""Cloudflare API utilities."""
import os
from typing import Optional
import aiohttp
from PIL import Image
import io

class CloudflareClient:
    def __init__(self, account_id: Optional[str] = None, api_token: Optional[str] = None):
        self.account_id = account_id or os.getenv("CLOUDFLARE_ACCOUNT_ID")
        self.api_token = api_token or os.getenv("CLOUDFLARE_API_TOKEN")
        if not self.account_id or not self.api_token:
            raise ValueError("未设置Cloudflare凭证")
            
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    async def generate_image(self, model_id: str, prompt: str, width: int, height: int, steps: int = None) -> Image.Image:
        """生成图像"""
        url = f"{self.base_url}/{model_id}"
        
        params = {
            "prompt": prompt,
            "width": width,
            "height": height
        }
        if steps:
            params["num_steps"] = steps
            
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=params) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API错误: {error_text}")
                
                image_data = await response.read()
                return Image.open(io.BytesIO(image_data))

    async def generate_prompt(self, theme: str) -> str:
        """使用AI生成提示词"""
        url = f"{self.base_url}/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b"
        
        system_prompt = """You are an expert at writing Stable Diffusion prompts..."""
        user_prompt = f"Create a highly detailed Stable Diffusion prompt for: {theme}"
        
        params = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=params) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"生成提示词失败: {error_text}")
                
                result = await response.json()
                return result.get("response", "").strip() 