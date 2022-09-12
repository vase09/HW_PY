from typing import Union


def get_filter(data: Union[list, map, filter, set], value: str) -> filter:
    check_type(data)
    if not isinstance(value, str):
        raise TypeError
    return filter(lambda line: value in line.lower(), data)


def get_map(data: Union[list, map, filter, set], value: Union[str, int]) -> map:
    check_type(data)
    try:
        value = int(value)
    except Exception:
        raise TypeError
    return map(lambda line: parse_string(line)[value - 1] + '\n', data)


def get_unique(data: Union[list, map, filter, set], value=None) -> set:
    check_type(data)
    return set(data)


def get_sort(data: Union[list, map, filter, set], value: str) -> list:
    check_type(data)
    if value not in ['asc', 'decs']:
        raise ValueError
    return sorted(data, reverse=(value == 'desc'))


def get_limit(data: Union[list, map, filter, set], value: Union[str, int]) -> list:
    check_type(data)
    print(type(data))
    try:
        value = int(value)
    except Exception:
        raise TypeError
    # return [text for num, text in enumerate(data, 1) if num <= int(value)]
    return list(data)[:value]


def parse_string(string: str) -> list:
    return string.split()


def check_type(data):
    if not isinstance(data, (list, map, filter, set)):
        raise TypeError
