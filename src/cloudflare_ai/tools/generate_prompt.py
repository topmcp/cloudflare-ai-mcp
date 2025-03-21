"""Prompt generation tools."""
from enum import Enum
from typing import List
from ..utils.cloudflare import CloudflareClient

class ImageTheme(str, Enum):
    BEAUTIFUL_GIRL = "a beautiful girl"
    HANDSOME_MAN = "a handsome man"
    FUTURE_CITY = "a future city"
    FANTASY_LANDSCAPE = "a fantasy landscape"
    CYBERPUNK_SCENE = "a cyberpunk scene"
    ANCIENT_CASTLE = "an ancient castle"

class PromptGenerator:
    def __init__(self, client: CloudflareClient):
        self.client = client

    async def generate_prompt(self, theme: str) -> str:
        """生成图像提示词"""
        return await self.client.generate_prompt(theme)

    def get_themes(self) -> List[str]:
        """获取所有预设主题"""
        return [theme.value for theme in ImageTheme] 