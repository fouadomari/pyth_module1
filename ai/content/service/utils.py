from ..content_clint import ContentClient


def validate_text(text: str, field_name: str, min_length: int) -> str:
    if not text or not text.strip():
        raise ValueError(f"{field_name} cannot be empty.")

    cleaned = text.strip()

    if len(cleaned) < min_length:
        raise ValueError(
            f"{field_name} must be at least {min_length} characters long."
        )

    return cleaned


def generate_content(prompt: str) -> str:
    client = ContentClient()
    result = client.generate(prompt)

    cleaned = result.strip() if result else ""

    if not cleaned:
        raise ValueError("The AI model returned empty content.")

    return cleaned