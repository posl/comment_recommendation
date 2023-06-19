def f(n, m, s, t):
    if n == 1:
        return -1
    elif n == 2:
        return -1
    elif n == 3:
        if m == 0:
            return s[0] + s[1] + s[2]
        else:
            return -1
    elif n == 4:
        if m == 0:
            return s[0] + s[1] + s[2] + s[3]
        else:
            return -1
    elif n == 5:
        if m == 0:
            return s[0] + s[1] + s[2] + s[3] + s[4]
        else:
            return -1
    elif n == 6:
        if m == 0:
            return s[0] + s[1] + s[2] + s[3] + s[4] + s[5]
        else:
            return -1
    elif n == 7:
        if m == 0:
            return s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6]
        else:
            return -1
    elif n == 8:
        if m == 0:
            return s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7]
        else:
            return -1
n, m = map(int, input().split())
s = []
t = []
for i in range(n):
    s.append(input())
for i in range(m):
    t.append(input())
print(f(n, m, s, t))
