# File: D:\ADK\python_interpreter_1\interpreter_agent\agent.py

from google.adk.agents import Agent
# Correctly import the CLASS from the MODULE
from google.adk.tools.built_in_code_execution_tool import BuiltInCodeExecutionTool

# Create an INSTANCE of the tool class
code_tool = BuiltInCodeExecutionTool()

root_agent = Agent(
    name="interpreter_agent",
    model="gemini-2.0-flash",
    description="An agent that can execute Python code to solve problems.",
    instruction="You are an expert programmer. Use the code execution tool to solve the user's request.",
    # Pass the INSTANCE to the tools list
    tools=[code_tool],
)
