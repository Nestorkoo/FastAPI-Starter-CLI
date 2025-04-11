from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="fastcli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "fastgen": [
            "config.py",
            "fastgen.config.yaml",
            
            "fastgen/templates/async/config.py.jinja",
            "fastgen/templates/async/database.py.jinja",
            "fastgen/templates/async/main.py.jinja",
            
            "fastgen/templates/sync/config.py.jinja",
            "fastgen/templates/sync/database.py.jinja",
            "fastgen/templates/sync/main.py.jinja",
            
            "utils/__init__.py",
            "utils/cli.py",
        ],
    },
    install_requires=[
        "click>=8.0.0", 
        "jinja2>=3.0.0",
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "PyYAML>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "fastcli=fastgen.cli:main",
        ],
    },
    author="Dmytro",
    author_email="nestorkodmytro@gmail.com",
    description="CLI tool for generating FastAPI projects with pre-configured architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="fastapi cli scaffolding jinja2",
    url="https://github.com/ваш-репозиторій/fastcli",  # Додайте посилання на репозиторій
)