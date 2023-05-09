def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**10
    for i in range(N):
        v = i
        s = 0
        p = []
        while True:
            v = P[v] - 1
            s += C[v]
            p.append(C[v])
            if v == i:
                break
        if s > 0:
            x = K // len(p)
            ans = max(ans, x * s + max(0, max(p)))
        else:
            ans = max(ans, max(p))
    print(ans)
