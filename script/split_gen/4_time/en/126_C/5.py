def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        c = 0
        while i < K:
            i *= 2
            c += 1
        ans += (1/N) * (1/2)**c
    print(ans)
