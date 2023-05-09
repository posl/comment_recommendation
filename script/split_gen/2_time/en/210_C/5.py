def main():
    #input
    N, K = map(int, input().split())
    Cs = list(map(int, input().split()))
    #compute
    #print(N, K, Cs)
    c = {}
    for i in range(K):
        if Cs[i] in c:
            c[Cs[i]] += 1
        else:
            c[Cs[i]] = 1
    ans = len(c)
    for i in range(K, N):
        c[Cs[i-K]] -= 1
        if c[Cs[i-K]] == 0:
            del c[Cs[i-K]]
        if Cs[i] in c:
            c[Cs[i]] += 1
        else:
            c[Cs[i]] = 1
        ans = max(ans, len(c))
    #output
    print(ans)
