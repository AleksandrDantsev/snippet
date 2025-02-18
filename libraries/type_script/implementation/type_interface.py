from utils.empty_or_val import empty_or_val
from..assets.abbreviations import abbr_interface_type_script
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.capitilize import capitalize


def type_interface(lst):
    empty_or_val(lst, 3)

    type_query, name, types = lst[:3]
    is_interface = abbr_interface_type_script == type_query


    formated_types = ";\n    ".join(types.split(", ")) + ";"
    type_or_interface = 'interface' if is_interface else 'type'

    head = "I" if is_interface else "T"
    quality = "" if is_interface else " ="

    return f"""{type_or_interface} {head}{capitalize(name)}{quality} {{
    {formated_types if types else ""}
}};"""


