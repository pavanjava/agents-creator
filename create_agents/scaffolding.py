import yaml
from create_agents.engines import phidata_engine, crewai_engine


def load_config(config_path):
    """
    Load configuration from a YAML file.
    """
    with open(config_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            raise ValueError(f"Error parsing YAML file: {exc}")


def scaffold_project(config_path, engine, project_name):
    """
    Scaffold the project using the specified engine.
    """
    config = load_config(config_path)

    if engine.lower() == "phidata":
        phidata_engine.scaffold(config, project_name)
    elif engine.lower() == "crewai":
        crewai_engine.scaffold(config)
    else:
        raise ValueError(f"Unsupported engine: {engine}")
