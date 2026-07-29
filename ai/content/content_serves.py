from ai.content.content_clint import ContentClient

# The prompt text must live in one place inside this file (e.g. a small private helper)
def _build_summary_prompt(text: str) -> str:
    return f"Please provide a concise summary of the following blog post:\n\n{text}"

def summarize_post(text: str) -> dict:
    """Runs the 4-stage summarization pipeline."""
    
    # 1. Input validation[cite: 1]
    if not text or not text.strip():
        raise ValueError("Content cannot be empty.")
    
    cleaned_input = text.strip()
    if len(cleaned_input) < 20:
        raise ValueError("Content must be at least 20 characters long.")

    # 2. AI processing[cite: 1]
    prompt = _build_summary_prompt(cleaned_input)
    client = ContentClient()
    raw_summary = client.generate(prompt)

    # 3. Post-processing[cite: 1]
    cleaned_summary = raw_summary.strip() if raw_summary else ""
    if not cleaned_summary:
        raise ValueError("The AI model returned an empty summary.")

    # 4. Response formatting[cite: 1]
    return {
        "summary": cleaned_summary,
        "length": len(cleaned_summary)
    }
    

# --- كود توليد المقالات الجديد ---

def _build_generation_prompt(title: str, tone: str = None) -> str:
    prompt = f"Write a short blog post about: {title}."
    if tone:
        prompt += f" Please use a {tone} tone."
    prompt += " The generated post must be strictly under 500 characters."
    return prompt

def generate_post(title: str, tone: str = None) -> dict:
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    
    cleaned_title = title.strip()
    if len(cleaned_title) < 5:
        raise ValueError("Title must be at least 5 characters long.")

    prompt = _build_generation_prompt(cleaned_title, tone)
    
    client = ContentClient()
    raw_content = client.generate(prompt)

    cleaned_content = raw_content.strip() if raw_content else ""
    if not cleaned_content:
        raise ValueError("The AI model returned empty content.")
        
    if len(cleaned_content) > 500:
        cleaned_content = cleaned_content[:500]

    return {
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }