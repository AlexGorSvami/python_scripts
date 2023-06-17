def recursive_unpacking_list(data: list) -> iter:
    for i in data:
        if isinstance(i, list):
            yield from recursive_unpacking_list(i)
        else:
            yield i


