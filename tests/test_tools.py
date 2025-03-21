"""Test cases for tools module."""
import pytest
from cloudflare_ai.tools import generate_images, generate_prompt

async def test_generate_images():
    result = await generate_images("test prompt", "1024x1024")
    assert isinstance(result, dict)

async def test_generate_prompt():
    result = await generate_prompt("test theme")
    assert isinstance(result, str) 