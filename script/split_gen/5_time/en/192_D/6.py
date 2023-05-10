def f(s, n):
    v = 0
    for i in s:
        v = v * n + int(i)
        if v > m:
            return False
    return True
s = input()
m = int(input())
d = int(max(s))
