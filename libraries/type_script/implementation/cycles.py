from utils.empty_or_val import empty_or_val
from utils.clean_marks import clean_marks
from..assets.abbreviations import abbr_cycle_for_IN, abbr_cycle_for_OF, abbr_cycle_while, abbr_cycle_do_while

# Возврящаемое значение в функции в виде аргумента lst: ['wd', 'count > 0', ..., ...]

# fi/i<element
# fi/i<element/--

def cycle_for_i(lst: list):
    empty_or_val(lst, 3)

    condition, counter = lst[1:3]

    if condition:
        condition = condition.replace(".length", "")
    
    counter = counter if counter in ["++", "--"] else "++"

    return f"""for (let i = 0; {condition or "i < collection"}.length; i{counter}) {{
	
}};"""





# ff/
# ff/var/store
# ff/var1,var2/lst    for of
# fn/var1,var2/lst    for in


def cycle_for_ofin(lst: list):

    empty_or_val(lst, 3)
    type_cycle, name, collection = lst[3]

    types = {
        abbr_cycle_for_IN: "in",
        abbr_cycle_for_OF: "of"
    }

    splitted_names = clean_marks(name, " ").split(",")
    collection = clean_marks(collection, " ").split(",")[0] or "collection"

    if len(splitted_names) > 1:
        name = f"[{', '.join(splitted_names[:2])}]"
        collection += ".entries()"

    return f"""for (let {name or "value"} {types[type_cycle]} {collection}) {{
        
}};"""




# wh/
# wh/item<20

def cycles_while(lst: list):
    empty_or_val(lst, 2)

    type_cycle = lst[0]
    condition = lst[1] or "false"

    if type_cycle == abbr_cycle_while:
        return f"""while ({condition}) {{
    
}};"""
    elif type_cycle == abbr_cycle_do_while:
        return f"""do {{

}} while ({condition});
"""