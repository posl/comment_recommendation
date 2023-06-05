def g_1(x):
    x = str(x)
    x_list = []
    for i in x:
        x_list.append(i)
    x_list.sort()
    x_list.reverse()
    x = ''.join(x_list)
    return int(x)

if __name__ == '__main__':
    g_1()