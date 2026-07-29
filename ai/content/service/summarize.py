from .utils import validate_text, generate_content

from blog.models import Post


def _build_summary_prompt(text: str) -> str:
    return (
        f"Please provide a concise summary of the following blog post:\n\n{text}"
    )


def summarize_post(text: str) -> dict:
    cleaned_text = validate_text(
        text=text,
        field_name="Content",
        min_length=20,
    )

    prompt = _build_summary_prompt(cleaned_text)
    summary = generate_content(prompt)

    return {
        "summary": summary,
        "length": len(summary),
    }
    

def summarize_post_by_id(post_id: int) -> dict:
    post = Post.objects.get(title_id=post_id)

    result = summarize_post(post.content)

    post.summary = result["summary"]
    post.save(update_fields=["summary"])

    return {
    "post_id": post.pk,
    "summary": post.summary,
    "length": result["length"],
}