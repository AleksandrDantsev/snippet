def capitalize(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:]