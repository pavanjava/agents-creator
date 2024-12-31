import os
from jinja2 import Template

# Agent template for PhiData
agent_template = """
from phi.agent import Agent
from phi.model.openai import OpenAIChat
{% for tool_import in tool_imports %}
{{ tool_import }}
{% endfor %}
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Define the model
model = OpenAIChat(id="{{ model_id }}")

# Define the tools
tools = [{% for tool in tools %}{{ tool }},{% endfor %}]

# Create the agent
{{ agent_name }} = Agent(
    name="{{ agent_name }}",
    model=model,
    tools=tools,
    add_history_to_messages={{ add_history }},
    markdown={{ markdown }},
    debug_mode={{debug_mode}}
)

{{ agent_name }}.print_response("Tell me about OpenAI Sora?", stream=True)
"""


def scaffold(config, proj_name):
    """
    Scaffolds a PhiData project based on the provided configuration.
    """
    project_name = config.get("project_name", proj_name)
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(f"{project_name}/agents", exist_ok=True)

    # Iterate through agents in the configuration
    for agent in config.get("agents", []):
        agent_code = generate_agent_code(agent)
        write_agent_file(agent['name'], agent_code, project_name)

    # Generate additional project files
    create_env_file(project_name)
    create_requirements_file(project_name)
    create_readme_file(project_name)

    print(f"Scaffolding completed for {project_name}.")


def generate_agent_code(agent_config):
    """
    Generate agent code using the Jinja2 template and provided agent configuration.
    """
    # Define the tool mappings for imports and function calls
    tool_mappings = {
        "DuckDuckGo": {
            "import": "from phi.tools.duckduckgo import DuckDuckGo",
            "call": "DuckDuckGo()",
        },
        "Yfinance": {
            "import": "from phi.tools.yfinance import YFinanceTools",
            "call": "YFinanceTools()",
        },
        # Add more tools as needed
    }

    # Generate tool imports and function calls
    tool_imports = []
    tools = []
    for tool in agent_config["tools"]:
        tool_type = tool["type"]
        if tool_type in tool_mappings:
            tool_imports.append(tool_mappings[tool_type]["import"])
            tools.append(tool_mappings[tool_type]["call"])

    # Remove duplicates from imports
    tool_imports = list(set(tool_imports))

    # Render the agent code using the template
    template = Template(agent_template)
    return template.render(
        agent_name=agent_config["name"].replace(" ", "_"),
        model_id=agent_config["model"]["id"],
        tool_imports=tool_imports,
        tools=tools,
        add_history=agent_config["add_history_to_messages"],
        markdown=agent_config["markdown"],
        debug_mode=agent_config["debug_mode"]
    )


def write_agent_file(agent_name: str, code: str, project_name: str):
    """
    Write the generated agent code to a Python file.
    """
    filename = f"{project_name}/agents/{agent_name.replace(' ', '_')}.py"
    with open(filename, "w") as file:
        file.write(code)


def create_env_file(project_name: str):
    """
    Create a .env file for environment variables.
    """
    env_content = """
# Environment variables
OPENAI_API_KEY=your-openai-api-key
"""
    with open(f"{project_name}/.env", "w") as file:
        file.write(env_content.strip())


def create_requirements_file(project_name: str):
    """
    Create a requirements.txt file for project dependencies.
    """
    requirements = [
        "phidata",
        "openai",
        "duckduckgo-search",
        "yfinance",
        "python-dotenv",
    ]
    with open(f"{project_name}/requirements.txt", "w") as file:
        file.write("\n".join(requirements))


def create_readme_file(project_name: str):
    """
    Create a README.md file with project information.
    """
    readme_content = f"""
# {project_name}
## Setup
        
1. Create a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate
```
        
2. Install dependencies:
```bash
pip install -r requirements.txt
```
        
3. Add your OpenAI API key to the `.env` file.
        
## Running Agents
        
Navigate to the `agents` directory and run the desired agent script:
```bash
cd agents
python agent_name.py
"""
    with open(f"{project_name}/README.md", "w") as file:
        file.write(readme_content.strip())
