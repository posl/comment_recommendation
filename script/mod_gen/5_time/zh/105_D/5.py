def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*N
    S[0] = A[0]
    for i in range(1,N):
        S[i] = S[i-1]+A[i]
    for i in range(N):
        S[i] = S[i]%M
    from collections import Counter
    cnt = Counter(S)
    ans = 0
    for v in cnt.values():
        ans += v*(v-1)//2
    ans += cnt[0]
    print(ans)

if __name__ == '__main__':
    solve()