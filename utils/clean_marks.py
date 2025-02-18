import re

def clean_marks(s: str, chars: str = '') -> str:
    return re.sub(f'[{re.escape(chars)}]', '', s)