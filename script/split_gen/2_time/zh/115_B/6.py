def solve():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    s = 0
    for i in range(n):
        if i == 0:
            s += p[i] // 2
        else:
            s += p[i]
    print(s)
