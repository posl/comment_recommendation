def func(n):
    s = str(n)
    if len(s) == 2:
        return n
    else:
        a = int(s[0])
        b = int(s[1:])
        return a*b

if __name__ == '__main__':
    func()