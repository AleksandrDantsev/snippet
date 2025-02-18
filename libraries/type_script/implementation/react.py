from utils.empty_or_val import empty_or_val
from utils.capitilize import capitalize
from utils.to_snake_case import to_snake_case
from..assets.abbreviations import abbr_react_template_type_script

create_template = lambda name, is_ts: f"""import React from "react";
import stl from "./{name}.module.scss";

{f"""interface {"I" + name} {{

}};""" if is_ts else ""}

const {name}{f": React.FC<{name}>" if is_ts else ""} = () => {{
    return (
        <div className={{stl.{to_snake_case(name)}_wrapper}}>
        
        </div>
    )
}}

export default {name};
"""


# r/
# r/name
# rt/
# rt/name

def react_template(lst: list):
    empty_or_val(lst, 2)
    
    type_query, name = lst[:2]

    if not name: name = "Component"

    return create_template(capitalize(name), type_query == abbr_react_template_type_script)

