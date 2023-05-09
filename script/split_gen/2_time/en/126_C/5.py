def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(1, N + 1):
        p = 1 / N
        j = i
        while j < K:
            j *= 2
            p /= 2
        ans += p
    print(ans)
