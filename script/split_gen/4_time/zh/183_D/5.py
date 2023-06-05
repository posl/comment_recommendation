def solve():
    n, w = map(int, input().split())
    a = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        a.append((s, p))
        a.append((t, -p))
    a.sort()
    s = 0
    for _, p in a:
        s += p
        if s > w:
            print("No")
            exit()
    print("Yes")
