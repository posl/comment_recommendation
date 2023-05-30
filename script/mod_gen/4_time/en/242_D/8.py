def f(s, t):
    if t == 0:
        return s
    if t % 2 == 0:
        return f(s, t // 2) + f(s, t // 2)
    else:
        return f(s, t // 2) + f(s, t // 2) + s
s = input()
q = int(input())
t = [0] * q
k = [0] * q
for i in range(q):
    t[i], k[i] = map(int, input().split())
    print(f(s, t[i])[k[i] - 1])
