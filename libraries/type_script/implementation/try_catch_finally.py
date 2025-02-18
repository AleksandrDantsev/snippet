from utils.empty_or_val import empty_or_val
from utils.capitilize import capitalize
from ..assets.abbreviations import abbr_try_catch_finally

# tc/
# tcf/error_message

def try_catch_finally(lst):
    empty_or_val(lst, 2)

    type_query, error_message = lst[:2]
    is_finally = type_query == abbr_try_catch_finally

    error_message_console = f'console.error("{capitalize(error_message)}", error.message)'

    result = f"""
try {{

}} catch(error) {{
    {error_message_console if error_message else ""}
}}{";" if not is_finally else ""} {"""finally {

};""" if is_finally else ""}
"""
    return result