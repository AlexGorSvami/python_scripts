def unpacking_list(array: list) -> list:
    new_list = array[:]
    index = 0
    while True:
        try:
            while isinstance(new_list[index], list):
                item = new_list.pop(index)
                for i in reversed(item):
                    new_list.insert(index, i)
            index += 1
        except IndexError:
            break
    return new_list



