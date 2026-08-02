from .utils import validate_text, generate_content
from .utils import  render_markdown

PROMPT_DIR = "../prompts"
PROMPT_TEMPLATE = "build_generation_prompt.md"

def _build_generation_prompt(title: str, tone: str = None) -> str:
    prompt = f"Write a short blog post about: {title}."
    
    if tone:
        prompt += f" Please use a {tone} tone."

    prompt += " The generated post must be strictly under 500 characters."

    return prompt


def generate_post(title: str, tone: str = None) -> dict:
    cleaned_title = validate_text(
        text=title,
        field_name="Title",
        min_length=5,
    )

    prompt = render_markdown(PROMPT_TEMPLATE, {"text": cleaned_title}, PROMPT_DIR)
    content = generate_content(prompt)

    if len(content) > 500:
        content = content[:500]

    return {
        "title": cleaned_title,
        "content": content,
        "length": len(content),
    }