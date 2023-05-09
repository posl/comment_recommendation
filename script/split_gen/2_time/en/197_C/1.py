def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(A[0] ^ A[1] ^ A[2])
        return
    
    ans = A[0] ^ A[1]
    for i in range(2, N):
        ans ^= A[i]
    print(ans)
solve()
