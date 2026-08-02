from ..content_clint import ContentClient
from jinja2 import Environment, FileSystemLoader
import os


def render_markdown(template_name: str, context: dict, template_dir: str) -> str:
    """Load a .md prompt TEMPLATE from disk and fill in its {{ placeholders }}.

    This is what lets every prompt live in its OWN .md file (one file per
    prompting technique) instead of being hardcoded in Python. Swap the file
    name and you swap the whole prompting strategy — this helper never changes.

    - template_dir is relative to THIS file, e.g. "../prompts".
    - context is the values for the template, e.g. {"text": "..."}.
    """
    absolute_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), template_dir))
    env = Environment(loader=FileSystemLoader(absolute_dir))
    template = env.get_template(template_name)
    return template.render(context)

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