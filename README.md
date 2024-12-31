# agents-creator
This repository is a tool that is agnostic of agentic framework to create agents from framework independent configuration

### How to Install
- `git clone https://github.com/pavanjava/agents-creator.git`
- `pip install -e .`

### How to run
- Open terminal and run `create-agents --project-name financial_agent --config config.yaml --engine phidata`

### Important Instructions
- find the sample `config.yaml` file in the `examples` directory.
- The `--engine` parameter can be one of the following: `phidata` or `crewai` (for this release only phidata is supported)
- replace your OpenAI API key in the `.env` file in the project root.

