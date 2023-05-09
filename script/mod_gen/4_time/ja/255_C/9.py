def count_operation(x, a, d, n):
    if d == 0:
        if x != a:
            return -1
        else:
            return 0
    else:
        if (x-a)%d != 0:
            return -1
        else:
            if (x-a)//d < 0:
                return -1
            else:
                if (x-a)//d < n:
                    return (x-a)//d
                else:
                    return -1

if __name__ == '__main__':
    count_operation()