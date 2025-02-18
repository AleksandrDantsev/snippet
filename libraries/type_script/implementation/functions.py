from utils.empty_or_val import empty_or_val
from..assets.abbreviations import (
    abbr_function_arrow_immediately, 
    abbr_function_declaration_immediately, 
    abbr_function_expression_immediately, 
    abbr_function_declaration, 
    abbr_function_expression
)

def func_cal_imm(func, current_type, ess_type):
    return f"({func})()" if (current_type == ess_type) else func




# fa/name/arg:n,arg1:s=24/:s|n

def func_arrow(list):
    empty_or_val(list, 4)

    type_func, name, args, ret_str = list[:4]
    FAM = abbr_function_arrow_immediately
    print(ret_str)

    
    if not name:
        return func_cal_imm(f"({args}){ret_str} => ()", type_func, FAM)
    

    declaration = f"const {name} = " if name else ""
    return_text = "return ;" if ret_str else ""


    return declaration + func_cal_imm(f"""({args}){ret_str} => {{
    {return_text}
}}""", type_func, FAM) + ";"




# fa/name/arg:n,arg1:s=24/r:s|n

def func_standart(list):
    empty_or_val(list, 4)

    type_func, name, args, ret_str = list[:4]

    FD = abbr_function_declaration
    FE = abbr_function_expression

    FDM = abbr_function_declaration_immediately
    FEM = abbr_function_expression_immediately


    # Function Declaration
    if type_func == FD or type_func == FDM:
        return func_cal_imm(f"""function {name}({args}){ret_str} {{
    return ;
}}""", type_func, FDM) + ";"
    

    # Function Experssion
    elif type_func == FE or type_func == FEM:

        declaration = f"const {name} = " if name else ""
        func_flesh = func_cal_imm(f"""function({args}){ret_str} {{
    return ;
}}""", type_func, FEM) + ";"

        return declaration + func_flesh