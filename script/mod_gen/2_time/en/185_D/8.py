def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(N+1)
    A.insert(0,0)
    B = []
    for i in range(1,M+2):
        if A[i]-A[i-1]-1 > 0:
            B.append(A[i]-A[i-1]-1)
    if len(B) == 0:
        print(0)
    else:
        K = min(B)
        for i in range(len(B)):
            if B[i] % K != 0:
                K = max(K,B[i]//2)
                break
        for i in range(len(B)):
            if B[i] % K != 0:
                K = B[i]
                break
        ans = 0
        for i in range(len(B)):
            ans += (B[i]-1)//K + 1
        print(ans)

if __name__ == '__main__':
    solve()