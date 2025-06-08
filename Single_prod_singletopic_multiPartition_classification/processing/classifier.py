def classify_text(text: str) -> str:
    spam_keywords = ["buy now", "free", "click here", "win"]
    for kw in spam_keywords:
        if kw in text:
            return "SPAM"
    return "HAM"