def calc(a):
    if len(a) == 1:
        return a
    elif len(a) == 2:
        if a[0] == '0' or a[1] == '0':
            return '0'
        else:
            return str(int(a[0]) * int(a[1]))
    else:
        max = 0
        for i in range(1, len(a)):
            if a[0] == '0' or a[i] == '0':
                continue
            else:
                if int(a[0]) * int(a[i]) > max:
                    max = int(a[0]) * int(a[i])
        if max == 0:
            return '0'
        else:
            return str(max)

if __name__ == '__main__':
    calc()