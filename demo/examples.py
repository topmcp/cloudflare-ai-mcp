"""Usage examples."""
import asyncio
from cloudflare_ai.tools import generate_images, generate_prompt

async def main():
    # Generate a detailed prompt
    prompt = await generate_prompt("fantasy landscape")
    print(f"Generated prompt: {prompt}")

    # Generate images using the prompt
    images = await generate_images(prompt, "1024x1024")
    print(f"Generated images: {images}")

if __name__ == "__main__":
    asyncio.run(main()) 