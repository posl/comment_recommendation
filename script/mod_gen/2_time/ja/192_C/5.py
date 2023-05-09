def g1(x):
    list_x = list(str(x))
    list_x.sort(reverse=True)
    str_x = "".join(list_x)
    return int(str_x)

if __name__ == '__main__':
    g1()