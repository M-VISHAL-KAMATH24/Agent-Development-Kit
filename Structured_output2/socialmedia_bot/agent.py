from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from typing import List

# --- Define the Output Schema ---
class SocialMediaPost(BaseModel):
    """
    A schema for generating a social media post in Markdown format.
    """
    platform: str = Field(
        description="The target social media platform (e.g., 'Twitter', 'LinkedIn', 'Instagram')."
    )
    content_markdown: str = Field(
        description="The full post content formatted in Markdown, including text, hashtags, and mentions."
    )
    hashtags: List[str] = Field(
        description="A list of relevant hashtags for the post, without the '#' symbol."
    )
    image_suggestion: str = Field(
        description="A brief, creative suggestion for an accompanying image (e.g., 'A vibrant sunset over a city skyline')."
    )

# --- Create the Social Media Agent ---
root_agent = LlmAgent(
    name="socialmedia_bot",
    model="gemini-2.0-flash", # Or any other model you're using
    description="Generates formatted social media posts with image suggestions.",
    instruction="""
        You are a Social Media Content Strategist.
        Based on the user's topic, generate a compelling post for a specific social media platform.

        GUIDELINES:
        - Adapt the tone and length for the specified platform (e.g., short and punchy for Twitter, professional for LinkedIn).
        - Format the main content using Markdown for emphasis (e.g., **bold**, *italics*).
        - Include a list of 3-5 relevant hashtags.
        - Suggest a visually appealing image that complements the post's message.

        Your response must be a single, valid JSON object that conforms to the required schema.
        Do not include any text outside of the JSON structure.
    """,
    output_schema=SocialMediaPost,
    output_key="social_post", # The key where the output will be stored
)
