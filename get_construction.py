from config_app import SEPARATOR
from libraries.type_script.assets.presentation_constructions import presentation_constructions
from libraries.type_script.assets.replacement_marks import replacement_marks
from utils.check_exist_element_in_dict import check_exist_element_in_dict
from utils.remove_all_spaces import remove_all_spaces
from utils.split_by_separator import split_by_separator
from .libraries.type_script.assets.presentation_constructions import abbr_try_catch, abbr_try_catch_finally
import re



def replace_types(text: str) -> str:
    for key in replacement_marks:
        if key != "marks":
            for old, new in replacement_marks[key].items():
                text = text.replace(old, new)

    for old, new in replacement_marks["marks"].items():
        if len(old) > 1:
            text = text.replace(old, new)


    for old, new in replacement_marks["marks"].items():
        if len(old) == 1:
            text = re.sub(rf"(?<=\S){re.escape(old)}(?=\S)", new, text)

    return text




def get_construction(line: str):
    if SEPARATOR not in line: return

    input_line = line
    
    if not any(word in input_line for word in [
        abbr_try_catch,
        abbr_try_catch_finally
    ]):
        input_line = remove_all_spaces(line)

    input_line = replace_types(input_line)
    splitted_input_line = split_by_separator(input_line, SEPARATOR)
    
    type_construction_el = splitted_input_line[0].lower()

    print(splitted_input_line)
 
    if check_exist_element_in_dict(type_construction_el, presentation_constructions):
        return presentation_constructions[type_construction_el](splitted_input_line)





