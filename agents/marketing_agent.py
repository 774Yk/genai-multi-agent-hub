from model import MarketingResponse, run_structured_agent


def run(user_prompt: str) -> dict:
    return run_structured_agent(
        schema=MarketingResponse,
        system_prompt=(
            "You are a digital marketing strategist. Transform the supplied source text "
            "into accurate, engaging content for X/Twitter and LinkedIn. Preserve the "
            "source meaning, avoid unsupported claims, and tailor each channel's tone."
        ),
        user_prompt=user_prompt,
    )
