# AI Image Generation MCP Server

> MCP Server for the Cloudflare AI API, enabling image generation operations with multiple models and prompt generation capabilities.

## Overview

This MCP server provides tools to generate images using Cloudflare's AI models while preserving quality and supporting multiple model types.

## Features

* **Multiple Model Support**: Supports various Stable Diffusion models from Cloudflare AI
* **Concurrent Generation**: Generate images with multiple models simultaneously
* **Prompt Generation**: AI-powered prompt generation for better results
* **Comprehensive Error Handling**: Clear error messages for common issues
* **Batch Operations**: Support for generating multiple images in parallel

## Tools

1. `generate_images`
   * Generate images using multiple models simultaneously
   * Inputs:
     * `prompt` (string): Image generation prompt
     * `size_id` (string): Image size (e.g., "1024x1024")
   * Returns: Dictionary of model IDs to generated images

2. `generate_prompt`
   * Generate detailed image prompts using AI
   * Inputs:
     * `theme` (string): Basic theme to expand
   * Returns: Detailed generation prompt

## Setup

### Prerequisites

- Python 3.10 or higher
- Sufficient disk space (1GB+ recommended)
- Stable network connection
- Cloudflare account and API token

### Cloudflare API Token

Create a Cloudflare API Token with appropriate permissions:

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Get Account ID:
   * Click account icon in top right
   * Select "Account Home"
   * Find "Account ID" in overview

3. Create API Token:
   * Go to "My Profile"
   * Select "API Tokens"
   * Click "Create Token"
   * Choose "Create Custom Token"
   * Add permissions:
     * Account.AI - Read & Edit
     * Account.Workers AI - Read & Edit

## Installation

### Option 1: Manual Installation via Configuration File

Add to your Claude Desktop config file:

* MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "CloudflareAI": {
      "command": "uvx",
      "args": ["cloudflare-ai"]
    }
  }
}
```

### Option 2: Automatic Installation via Smithery

```bash
npx -y @smithery/cli install cloudflare-ai --client claude
```

## Development

### Building and Publishing

```bash
# Sync dependencies
uv sync

# Build package
uv build

# Publish to PyPI
uv publish
```

### Debugging

For the best debugging experience, use the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector python serv.py
```

## Project Structure

```
cloudflare-ai/
├── src/
│   └── cloudflare_ai/
│       ├── __init__.py
│       ├── server.py
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── generate_images.py
│       │   └── generate_prompt.py
│       └── utils/
│           ├── __init__.py
│           ├── cloudflare.py
│           └── logging.py
├── demo/
│   └── examples.py
├── tests/
│   └── test_tools.py
├── pyproject.toml
├── uv.lock
├── README.md
└── README_CN.md
```

## Configuration

### Local Development

1. Copy example config:
```bash
cp .env.example .env
```

2. Edit configuration:
```env
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
```

### Production Environment

For production, use environment variables:

```bash
# Linux/Mac
export CLOUDFLARE_ACCOUNT_ID="your_account_id"
export CLOUDFLARE_API_TOKEN="your_api_token"

# Windows
set CLOUDFLARE_ACCOUNT_ID=your_account_id
set CLOUDFLARE_API_TOKEN=your_api_token
```

## Running the Server

### MCP Client Configuration

Add the following configuration to your MCP client settings:

```json
{
  "mcpServers": {
    "CloudflareAI": {
      "command": "python",
      "args": ["serv.py"],
      "env": {
        "CLOUDFLARE_ACCOUNT_ID": "your_account_id",
        "CLOUDFLARE_API_TOKEN": "your_api_token"
      },
      "cwd": "/path/to/server/directory"
    }
  }
}
```

Configuration options:
* `command`: Python executable path
* `args`: Server script and arguments
* `env`: Environment variables for authentication
* `cwd`: Working directory for the server

You can also use the server with custom port:
```json
{
  "mcpServers": {
    "CloudflareAI": {
      "command": "python",
      "args": ["serv.py", "--port", "8080"],
      "env": {
        "CLOUDFLARE_ACCOUNT_ID": "your_account_id",
        "CLOUDFLARE_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

### Development Mode

```bash
# Run server in test mode
python serv.py
```

### Production Deployment

Using uvicorn or gunicorn:

1. Install server:
```bash
pip install uvicorn gunicorn
```

2. Run with uvicorn:
```bash
uvicorn serv:app --host 0.0.0.0 --port 8000 --workers 4
```

3. Or with gunicorn (Linux/Mac only):
```bash
gunicorn serv:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## Monitoring & Logging

### Log Configuration

Create `logging.conf`:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    ]
)
```

### Performance Monitoring

Recommended tools:
- Prometheus + Grafana
- New Relic
- Datadog

## Security Recommendations

1. Use HTTPS
2. Implement rate limiting
3. Keep dependencies updated
4. Never hardcode credentials
5. Set proper file permissions

## Troubleshooting

### Common Issues

1. API Credential Errors:
   * Verify Account ID and API Token
   * Check token permissions

2. Network Issues:
   * Check firewall settings
   * Verify network connectivity

3. Memory Issues:
   * Adjust worker count
   * Monitor memory usage

### Debug Mode

```bash
# Run with debug mode enabled
DEBUG=1 python serv.py
```

## Maintenance

1. Update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

2. Monitor Cloudflare API changes
3. Monitor disk usage
4. Backup configuration files regularly

## Support

For assistance:
1. Check documentation
2. Submit GitHub Issue
3. Contact technical support

## License

This MCP server is licensed under the MIT License. 