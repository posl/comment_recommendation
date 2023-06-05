def median(lst):
    if len(lst) == 0:
        return None
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return lst[int(len(lst) / 2)]
    else:
        return lst[int(len(lst) / 2 - 1)]
