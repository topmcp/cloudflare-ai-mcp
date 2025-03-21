将 Python 项目打包并发布到 PyPI 的主要步骤：

## 1. 项目结构准备

基本的项目结构应该是:

```
project_root/
├── LICENSE
├── pyproject.toml  
├── README.md
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── module.py
└── tests/
```

## 2. 必要文件配置

### pyproject.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "package_name"
version = "0.0.1"
authors = [
  { name="Author Name", email="author@example.com" },
]
description = "Package description"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/username/project"
```

### README.md
包含项目描述、安装和使用说明等信息。

### LICENSE
选择合适的开源许可证(如 MIT License)。

## 3. 构建分发包

1. 安装构建工具:
```bash
python -m pip install --upgrade build
```

2. 构建分发包:
```bash
python -m build
```

这会在 `dist/` 目录下生成:
- `.whl` 文件(构建分发包)
- `.tar.gz` 文件(源码分发包)

## 4. 上传到 PyPI

1. 注册 PyPI 账号:
- 测试: https://test.pypi.org
- 正式: https://pypi.org

2. 创建 API token

3. 安装上传工具:
```bash
python -m pip install --upgrade twine
```

4. 上传到测试 PyPI:
```bash
python -m twine upload --repository testpypi dist/*
```

5. 上传到正式 PyPI:
```bash
python -m twine upload dist/*
```

## 5. 验证安装

从 TestPyPI 安装:
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps package_name
```

从正式 PyPI 安装:
```bash
pip install package_name
```

## 重要提示

1. 包名必须是唯一的,不能与 PyPI 上已有的包重名

2. 版本号要遵循语义化版本规范

3. 正式发布前建议先在 TestPyPI 上测试

4. 确保所有必要的依赖都在 pyproject.toml 中声明

5. 上传前检查构建包的完整性

[Source](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
