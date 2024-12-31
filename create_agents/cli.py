import typer
from pathlib import Path
from create_agents.scaffolding import scaffold_project

app = typer.Typer(help="A CLI tool to scaffold agent-based projects.")


@app.command()
def create_agents(
        config: str = typer.Option(..., help="Path to the YAML configuration file"),
        engine: str = typer.Option(..., help="Engine to use for scaffolding (e.g., phidata, crewai)"),
        project_name: str = typer.Option(..., help="Name of the project to be created")
):
    """
    CLI command to scaffold agents based on the provided configuration and engine.
    """
    config_path = Path(config)
    if not config_path.is_file():
        typer.echo(f"Configuration file {config} not found.")
        raise typer.Exit(code=1)

    scaffold_project(config_path, engine, project_name)
    typer.echo(f"Agents created successfully using engine: {engine}.")


if __name__ == "__main__":
    app()
