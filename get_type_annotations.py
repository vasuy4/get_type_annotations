from typing import Dict, Union, Set, Any, List


def get_type_annotation(obj: Any) -> str:
    """
    Возвращает строку с аннотацией типа для переданного объекта.

    :param obj: Объект, для которого нужно определить аннотацию типа.
    :return: Строка с аннотацией типа в формате Dict[str, Union[...]]
    """
    result: str = ""
    if type(obj) is dict:
        set_types_keyes: Set[str] = {get_type_annotation(k) for k in obj.keys()}
        set_types_values: Set[str] = {get_type_annotation(v) for v in obj.values()}
        if len(set_types_keyes) > 1:
            result += f"Dict[Union[{", ".join(set_types_keyes if set_types_keyes else "Any")}], "
        else:
            result += f"Dict[{set_types_keyes.pop()}, "
        if len(set_types_values) > 1:
            result += f"Union[{", ".join(set_types_values)}]]"
        else:
            result += f"{set_types_values.pop() if set_types_values else "Any"}]"
    elif type(obj) is list:
        set_types: Set[str] = {get_type_annotation(v) for v in obj}
        if len(set_types) > 1:
            result += f"List[Union[{", ".join(set_types)}]]"
        else:
            result += f"List[{set_types.pop() if set_types else "Any"}]"
    else:
        return str(type(obj).__name__)
    return result
