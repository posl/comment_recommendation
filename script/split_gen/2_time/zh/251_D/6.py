def solve():
    n = int(input())
    s_t = []
    for i in range(n):
        s, t = input().split()
        s_t.append((s, int(t), i + 1))
    s_t.sort(key=lambda x: (x[0], -x[1]))
    print(s_t[-1][2])
