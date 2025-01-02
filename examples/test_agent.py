from phi.agent import Agent
from phi.model.openai import OpenAIChat
from rich.prompt import Prompt
from typing import Optional
import typer

from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Define the model
model = OpenAIChat(id="gpt-4o")

# Define the tools
tools = [DuckDuckGo(), YFinanceTools(), ]


# Create the agent
def Financial_Search_Agent(user: str = "user"):
    run_id: Optional[str] = None
    Financial_Search_Agent = Agent(
        name="Financial_Search_Agent",
        user_id=user,
        model=model,
        tools=tools,
        add_history_to_messages=True,
        markdown=False,
        debug_mode=True
    )
    if run_id is None:
        run_id = Financial_Search_Agent.run_id
        print(f"Started Run: {run_id}")
    else:
        print(f"Continuing Run: {run_id}")
    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        Financial_Search_Agent.print_response(message, stream=True)


if __name__ == "__main__":
    typer.run(Financial_Search_Agent)
