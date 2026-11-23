"""Shared LangChain model integration and structured output schemas."""
from typing import Any, Type

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from config import (
    APP_URL,
    MAX_TOKENS,
    MODEL_ID,
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    TEMPERATURE,
)


class SupportResponse(BaseModel):
    summary: str = Field(description="A concise summary of the customer's issue")
    category: str = Field(description="Issue category such as billing, technical, account, or other")
    sentiment: str = Field(description="positive, neutral, or negative")
    response: str = Field(description="A professional response to the customer")
    next_step: str = Field(description="The recommended next action for the support representative")


class MarketingResponse(BaseModel):
    summary: str = Field(description="A concise summary of the source content")
    hook: str = Field(description="A compelling marketing hook")
    twitter_post: str = Field(description="A short post for X/Twitter with relevant hashtags")
    linkedin_post: str = Field(description="A polished professional LinkedIn post")
    call_to_action: str = Field(description="A clear call to action")


class TutorResponse(BaseModel):
    language: str = Field(description="The programming language detected")
    error_analysis: str = Field(description="A concise explanation of the likely issue")
    hint: str = Field(description="A step-by-step hint that guides the learner without giving the complete fixed code")
    concept: str = Field(description="The programming concept the learner should review")
    next_question: str = Field(description="A question that encourages the learner to continue debugging")


llm = ChatOpenAI(
    model=MODEL_ID,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
    default_headers={
        "HTTP-Referer": APP_URL,
        "X-Title": "GenAI Multi-Agent Workspace",
    },
)


def run_structured_agent(
    *,
    system_prompt: str,
    user_prompt: str,
    schema: Type[BaseModel],
) -> dict[str, Any]:
    """Create a reusable PromptTemplate | LLM | JsonOutputParser chain."""
    parser = JsonOutputParser(pydantic_object=schema)
    prompt = PromptTemplate(
        template=(
            "System instructions:\n{system_prompt}\n\n"
            "{format_instructions}\n\n"
            "User input:\n{user_prompt}"
        ),
        input_variables=["system_prompt", "user_prompt"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | llm | parser
    result = chain.invoke({"system_prompt": system_prompt, "user_prompt": user_prompt})
    return result if isinstance(result, dict) else result.model_dump()
