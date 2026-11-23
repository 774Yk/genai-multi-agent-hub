from model import TutorResponse, run_structured_agent


def run(user_prompt: str) -> dict:
    return run_structured_agent(
        schema=TutorResponse,
        system_prompt=(
            "You are a patient programming tutor. Diagnose the learner's code and guide "
            "them with progressive hints. Do not provide the complete corrected solution "
            "unless the user explicitly asks after attempting the hints. Encourage debugging "
            "and explain the underlying concept clearly."
        ),
        user_prompt=user_prompt,
    )
