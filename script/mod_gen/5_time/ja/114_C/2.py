def f(n, s):
    if n > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += f(10 * n + int(c), s + c)
    return ret
N = int(input())
print(f(0, ''))

if __name__ == '__main__':
    f()