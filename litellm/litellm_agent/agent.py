import os
import random

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

# The model string should not include 'openrouter/'
# LiteLLM handles the routing based on the model name.
model = LiteLlm(
    model="openrouter/x-ai/grok-4-fast:free",
 #provider/model family/model
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def get_dad_joke():
    """Returns a random dad joke."""
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)

# It's good practice to wrap simple functions in a FunctionTool
dad_joke_tool = FunctionTool(func=get_dad_joke)

root_agent = Agent(
    name="litellm_agent",
    model=model,
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes.
    Only use the tool `get_dad_joke` to tell jokes.
    """,
    # Pass the FunctionTool instance to the tools list
    tools=[dad_joke_tool],
)
