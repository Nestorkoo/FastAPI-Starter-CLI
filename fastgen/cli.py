import typer
import yaml
from fastgen.utils.generator import generate_project
from pathlib import Path
from importlib import resources

app = typer.Typer()

@app.command()
def init():
    """Initialize a default configuration file"""
    try:
        template = resources.read_text("fastgen", "fastgen.config.yaml")
        config_path = Path("fastgen.config.yaml")
        
        if config_path.exists():
            typer.echo("Error: Configuration file already exists.", err=True)
            raise typer.Exit(code=1)
            
        config_path.write_text(template, encoding="utf-8")
        typer.echo("✅ Configuration file created successfully!")
        
    except Exception as e:
        typer.echo(f"Error: Failed to create config file - {e}", err=True)
        raise typer.Exit(code=1)
@app.command()
def create(
    config: Path = typer.Option(None, "-c", "--config", help="Path to config file")
):
    """Create a new project from configuration"""
    try:
        if not config.exists():
            typer.echo(f"Error: Config file '{config}' not found.", err=True)
            raise typer.Exit(code=1)
        
        conf = yaml.safe_load(config.read_text())
        
        if not conf.get("project"):
            typer.echo("Error: Invalid config - missing 'project' section", err=True)
            raise typer.Exit(code=1)
            
        project_conf = conf["project"]
        
        generate_project(
            name=project_conf["name"],
            async_mode=project_conf.get("async", False),
            with_auth=conf.get("auth", {}).get("enabled", False),
            with_docker=conf.get("docker", {}).get("enabled", False),
            db_type=conf.get("database", {}).get("type", "sqlite")
        )
        
        typer.echo(f"✅ Project '{project_conf['name']}' created successfully!")
        
    except yaml.YAMLError as e:
        typer.echo(f"Error: Invalid YAML - {e}", err=True)
        raise typer.Exit(code=1)
    except KeyError as e:
        typer.echo(f"Error: Missing required config key - {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


def main():
    app()

if __name__ == "__main__":
    app()
