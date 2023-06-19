def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 200
    b = [[] for _ in range(mod)]
    c = [[] for _ in range(mod)]
    for i in range(1, 1 << n):
        s = 0
        for j in range(n):
            if i >> j & 1:
                s += a[j]
                s %= mod
        if len(b[s]) == 0:
            b[s] = [j + 1 for j in range(n) if i >> j & 1]
        else:
            c[s] = [j + 1 for j in range(n) if i >> j & 1]
            break
    if len(c[s]) == 0:
        print("No")
    else:
        print("Yes")
        print(len(b[s]), *b[s])
        print(len(c[s]), *c[s])

if __name__ == '__main__':
    solve()