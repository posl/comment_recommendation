def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                print(A[i]+A[j])
                return
    print(-1)
    return
