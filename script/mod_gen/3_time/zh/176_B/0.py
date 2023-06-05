def f(s):
    if len(s) == 1:
        return s
    else:
        return int(s[0]) + f(s[1:])
n = input()

if __name__ == '__main__':
    f()