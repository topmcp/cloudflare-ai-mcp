# AI 图像生成 MCP 服务器

> 基于 Cloudflare AI API 的 MCP 服务器，支持多模型图像生成操作和提示词生成功能。

## 概述

本 MCP 服务器提供工具，使用 Cloudflare 的 AI 模型生成图像，同时保持质量并支持多种模型类型。

## 功能特点

* **多模型支持**：支持 Cloudflare AI 提供的多种 Stable Diffusion 模型
* **并发生成**：同时使用多个模型生成图像
* **提示词生成**：AI 驱动的提示词生成，获得更好的效果
* **全面错误处理**：清晰的常见错误提示信息
* **批量操作**：支持并行生成多张图像

## 工具

1. `generate_images`
   * 同时使用多个模型生成图像
   * 输入参数：
     * `prompt` (字符串)：图像生成提示词
     * `size_id` (字符串)：图像尺寸（如 "1024x1024"）
   * 返回值：模型 ID 到生成图像的字典映射

2. `generate_prompt`
   * 使用 AI 生成详细的图像提示词
   * 输入参数：
     * `theme` (字符串)：基础主题
   * 返回值：详细的生成提示词

## 环境准备

### 系统要求

- Python 3.10 或更高版本
- 足够的磁盘空间（建议 1GB 以上）
- 稳定的网络连接
- Cloudflare 账号和 API 令牌

### Cloudflare API 令牌

创建具有适当权限的 Cloudflare API 令牌：

1. 登录 [Cloudflare 控制台](https://dash.cloudflare.com)
2. 获取账号 ID：
   * 点击右上角账号图标
   * 选择"账号主页"
   * 在概览中找到"账号 ID"

3. 创建 API 令牌：
   * 进入"我的个人资料"
   * 选择"API 令牌"
   * 点击"创建令牌"
   * 选择"创建自定义令牌"
   * 添加权限：
     * Account.AI - 读取和编辑
     * Account.Workers AI - 读取和编辑

## 安装

### 方式一：通过配置文件手动安装

将以下配置添加到 Claude Desktop 配置文件中：

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

### 方式二：通过 Smithery 自动安装

```bash
npx -y @smithery/cli install cloudflare-ai --client claude
```

## 开发

### 构建和发布

```bash
# 同步依赖
uv sync

# 构建包
uv build

# 发布到 PyPI
uv publish
```

### 调试

使用 MCP Inspector 获得最佳调试体验：

```bash
npx @modelcontextprotocol/inspector python serv.py
```

## 项目结构

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

## 配置

### 本地开发

1. 复制示例配置：
```bash
cp .env.example .env
```

2. 编辑配置：
```env
CLOUDFLARE_ACCOUNT_ID=你的账号ID
CLOUDFLARE_API_TOKEN=你的API令牌
```

### 生产环境

在生产环境中，使用环境变量：

```bash
# Linux/Mac
export CLOUDFLARE_ACCOUNT_ID="你的账号ID"
export CLOUDFLARE_API_TOKEN="你的API令牌"

# Windows
set CLOUDFLARE_ACCOUNT_ID=你的账号ID
set CLOUDFLARE_API_TOKEN=你的API令牌
```

## 运行服务器

### MCP 客户端配置

将以下配置添加到你的 MCP 客户端设置中：

```json
{
  "mcpServers": {
    "CloudflareAI": {
      "command": "python",
      "args": ["serv.py"],
      "env": {
        "CLOUDFLARE_ACCOUNT_ID": "你的账号ID",
        "CLOUDFLARE_API_TOKEN": "你的API令牌"
      },
      "cwd": "/path/to/server/directory"
    }
  }
}
```

配置选项：
* `command`：Python 可执行文件路径
* `args`：服务器脚本和参数
* `env`：认证环境变量
* `cwd`：服务器工作目录

你也可以使用自定义端口：
```json
{
  "mcpServers": {
    "CloudflareAI": {
      "command": "python",
      "args": ["serv.py", "--port", "8080"],
      "env": {
        "CLOUDFLARE_ACCOUNT_ID": "你的账号ID",
        "CLOUDFLARE_API_TOKEN": "你的API令牌"
      }
    }
  }
}
```

### 开发模式

```bash
# 在测试模式下运行服务器
python serv.py
```

### 生产部署

使用 uvicorn 或 gunicorn：

1. 安装服务器：
```bash
pip install uvicorn gunicorn
```

2. 使用 uvicorn 运行：
```bash
uvicorn serv:app --host 0.0.0.0 --port 8000 --workers 4
```

3. 或使用 gunicorn（仅限 Linux/Mac）：
```bash
gunicorn serv:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## 监控和日志

### 日志配置

创建 `logging.conf`：
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

### 性能监控

推荐工具：
- Prometheus + Grafana
- New Relic
- Datadog

## 安全建议

1. 使用 HTTPS
2. 实现速率限制
3. 保持依赖包更新
4. 不要硬编码凭证
5. 设置适当的文件权限

## 故障排除

### 常见问题

1. API 凭证错误：
   * 验证账号 ID 和 API 令牌
   * 检查令牌权限

2. 网络问题：
   * 检查防火墙设置
   * 验证网络连接

3. 内存问题：
   * 调整工作进程数量
   * 监控内存使用情况

### 调试模式

```bash
# 启用调试模式运行
DEBUG=1 python serv.py
```

## 维护

1. 更新依赖：
```bash
pip install --upgrade -r requirements.txt
```

2. 监控 Cloudflare API 变更
3. 监控磁盘使用情况
4. 定期备份配置文件

## 支持

如需帮助：
1. 查看文档
2. 提交 GitHub Issue
3. 联系技术支持

## 许可证

本 MCP 服务器基于 MIT 许可证开源。 