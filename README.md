# FastAPI Project Generator

A powerful and flexible CLI tool for scaffolding FastAPI projects with built-in support for database migrations (Alembic), async or sync project structure, and easy configuration using a simple YAML file.

## 🚀 Features

- Generate complete FastAPI project structure
- Support for **async** or **sync** project styles
- Optional **Alembic** integration for database migrations
- Templated structure using **Jinja2**
- Easily configurable via YAML
- Ready-to-use CLI with Typer

## 📦 Installation
```bash
git clone https://github.com/Nestorkoo/FastAPI-Starter-CLI.git
```
```bash
pip install -r requirements.txt
```
```bash
pip install -e .
```
- After this command you can run the CLI from anywhere
## 🔑 How to use?

```bash
fastcli init
```
- This command will create a configure file, which you can edit to your requirements
```bash
fastcli create --config fastgen.config.yaml
```
- Finally, you get your project, don't forget to setting you alembic files!
