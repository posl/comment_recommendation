def solve():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s_t = sorted(zip(s, t), key=lambda x: x[0])
    s, t = zip(*s_t)
    ans = [0] * n
    ans[0] = t[0]
    for i in range(1, n):
        ans[i] = min(ans[i - 1] + s[i - 1], t[i])
    for i in range(n):
        print(ans[i])
