def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
            continue
        tmp = 1/N
        j = i
        while j < K:
            j *= 2
            tmp /= 2
        ans += tmp
    print(ans)
