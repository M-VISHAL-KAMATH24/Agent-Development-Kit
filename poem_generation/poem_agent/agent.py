
import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Model configuration remains the same
model = LiteLlm(
    model="openrouter/nvidia/nemotron-nano-9b-v2:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


# --- Agent Definition ---
root_agent = Agent(
    name="poem_agent", # Renamed for clarity
    model=model,
    description="A creative agent that writes poems.",
    instruction="""
    You are a talented poet. When the user provides a word or a topic,
    your task is to write a short, creative poem about it.
    """,
    # The tools list is now empty because the LLM will do the work itself.
    tools=[],
)
