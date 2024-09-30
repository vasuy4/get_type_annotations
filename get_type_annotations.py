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
        len_keys: int = len(set_types_keyes)
        len_values: int = len(set_types_values)
        if len_keys > 1:
            result += f"Dict[Union[{", ".join(set_types_keyes)}], "
        elif len_keys == 1:
            result += f"Dict[{set_types_keyes.pop()}, "
        if len_values > 1:
            result += f"Union[{", ".join(set_types_values)}]]"
        elif len_values == 1:
            result += f"{set_types_values.pop()}]"
    elif type(obj) is list:
        set_types: Set[str] = {get_type_annotation(v) for v in obj}
        len_set: int = len(set_types)
        if len_set > 1:
            result += f"List[Union[{", ".join(set_types)}]]"
        elif len_set == 1:
            result += f"List[{set_types.pop()}]"
    else:
        return str(type(obj).__name__)
    return result
