def main():
    import math
    N, K = map(int, input().split())
    if K == 1:
        print(1)
        return
    ans = 0
    for i in range(1, N+1):
        x = i
        cnt = 0
        while x < K:
            x *= 2
            cnt += 1
        ans += 1/N * (1/2)**cnt
    print(ans)
