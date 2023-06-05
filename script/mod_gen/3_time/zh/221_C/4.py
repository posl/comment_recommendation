def split_num(n):
    num = [int(i) for i in str(n)]
    l = len(num)
    max = 0
    for i in range(1, l):
        a = num[:i]
        b = num[i:]
        if a[0] == 0 or b[0] == 0:
            continue
        a = int(''.join(str(i) for i in a))
        b = int(''.join(str(i) for i in b))
        if a * b > max:
            max = a * b
    return max

if __name__ == '__main__':
    split_num()