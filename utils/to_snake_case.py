import re

def to_snake_case(name: str) -> str:
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name).lower()
