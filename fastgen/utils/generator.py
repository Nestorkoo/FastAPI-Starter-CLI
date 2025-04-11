from pathlib import Path
from jinja2 import Environment, PackageLoader, TemplateNotFound
import shutil
from importlib import resources

def render_template(template_path: str, context: dict) -> str:
    env = Environment(loader=PackageLoader("fastgen", "templates"))
    try:
        template = env.get_template(template_path)
    except TemplateNotFound:
        raise ValueError(f"Template '{template_path}' not found")
    return template.render(context)

def generate_project(
    name: str, async_mode: bool, with_auth: bool, with_docker: bool, db_type: str
):
    if not name:
        raise ValueError("Project name is required")

    template_type = "async" if async_mode else "sync"
    base_path = Path(name)

    files_to_create = {
        "app/main.py": f"{template_type}/main.py.jinja",
        "app/config.py": f"{template_type}/config.py.jinja",
        "app/database.py": f"{template_type}/database.py.jinja",
        'app/routers/__init__.py': None,
        "app/services/__init__.py": None,
        "app/models/__init__.py": None,
        "app/schemas/__init__.py": None,
        "app/utils/__init__.py": None,
        ".env": f"{template_type}/.env.jinja",
        "requirements.txt": "fastapi\nuvicorn\n",
    }

    if with_auth:
        files_to_create["app/auth.py"] = f"{template_type}/auth.py.jinja"
        if with_docker:
            files_to_create["docker-compose.yml"] = "docker-compose.yml.jinja"

    for file_path, template in files_to_create.items():
        full_path = base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        if template and template.endswith(".jinja"):
            content = render_template(
                template,
                {
                    "project_name": name,
                    "db_type": db_type,
                    "with_auth": with_auth,
                    "with_docker": with_docker,
                },
            )
        else:
            content = template or ""

        with full_path.open("w", encoding="utf-8") as f:
            f.write(content)
