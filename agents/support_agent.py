from model import SupportResponse, run_structured_agent


def run(user_prompt: str) -> dict:
    return run_structured_agent(
        schema=SupportResponse,
        system_prompt=(
            "You are an empathetic customer support specialist. Classify the issue, "
            "identify the sentiment, and draft a helpful professional reply. "
            "Do not invent account details, policies, refunds, or promises."
        ),
        user_prompt=user_prompt,
    )
