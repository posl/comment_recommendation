def solve():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if N < K:
        print("-1")
        return
    if K == 1:
        if A[0] % D == 0:
            print("-1")
        else:
            print(A[0])
        return
    ans = -1
    for i in range(N-K+1):
        if A[i] % D == 0:
            continue
        ans = max(ans, A[i+K-1])
    print(ans)
    return

if __name__ == '__main__':
    solve()