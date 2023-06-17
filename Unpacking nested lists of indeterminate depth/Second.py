def unpacking_list(array: list) -> list:
    flag = True

    while flag:
        res = []
        flag = False
        for i in array:
            if isinstance(i, list):
                res.extend(i)
                flag = True
            else:
                res.append(i)
        array = res
    return res


