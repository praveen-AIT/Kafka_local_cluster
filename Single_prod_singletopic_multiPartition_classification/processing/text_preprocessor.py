def preprocess_text(text: str) -> str:
    import re
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text