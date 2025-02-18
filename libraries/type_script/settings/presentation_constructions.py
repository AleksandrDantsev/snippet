from ..implementation.variable import variable
from ..implementation.cycles import cycle_for_i, cycle_for_ofin, cycles_while
from ..implementation.functions import func_arrow, func_standart
from ..implementation.react import react_template
from ..implementation.type_interface import type_interface
from ..implementation.try_catch_finally import try_catch_finally
from .abbreviations import *


presentation_constructions = {
    # Функции
    abbr_function_declaration: func_standart,
    abbr_function_expression: func_standart,
    abbr_function_arrow: func_arrow,

    # Функции самовызыв.
    abbr_function_declaration_immediately: func_standart,
    abbr_function_expression_immediately: func_standart,
    abbr_function_arrow_immediately: func_arrow,

    # Класс
    abbr_class_declaration: None, 

    # Циклы
    abbr_cycle_for: cycle_for_i,
    abbr_cycle_for_IN: cycle_for_ofin,
    abbr_cycle_for_OF: cycle_for_ofin,
    abbr_cycle_while: cycles_while,
    abbr_cycle_do_while: cycles_while,

    # Обработчики ошибок
    abbr_try_catch: try_catch_finally,
    abbr_try_catch_finally: try_catch_finally,

    # React
    abbr_react_template: react_template,
    abbr_react_template_type_script: react_template,

    # Переменные
    abbr_const: variable,
    abbr_let: variable,
    abbr_var: variable,

    # Типизация
    abbr_interface_type_script: type_interface,
    abbr_type_type_script: type_interface,
}