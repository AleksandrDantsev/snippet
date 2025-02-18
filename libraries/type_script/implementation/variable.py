from utils.empty_or_val import empty_or_val
from..assets.abbreviations import abbr_const, abbr_let, abbr_var

# c/item;
# v/item:n/;
# l/age:n/23;

def variable(list: list):
    empty_or_val(list, 3)

    variables = {
        abbr_const: "const",
        abbr_let: "let",
        abbr_var: "var",
    }

    query_type, name, value = list[:3] 

    return f"{variables[query_type]} {name} = {value};"

