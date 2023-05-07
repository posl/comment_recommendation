def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    if N == K:
        print(len(set(C)))
        return
    C = C + C
    d = {}
    for i in range(K):
        if C[i] in d:
            d[C[i]] += 1
        else:
            d[C[i]] = 1
    ans = len(d)
    for i in range(K, N):
        d[C[i]] += 1
        if d[C[i]] == 1:
            ans += 1
        d[C[i-K]] -= 1
        if d[C[i-K]] == 0:
            ans -= 1
        if ans == K:
            print(K)
            return
    print(ans)
main()
