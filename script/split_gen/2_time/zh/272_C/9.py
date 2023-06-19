def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            if (A[i] + A[j]) % 2 == 0:
                print(A[i] + A[j])
                return
    print(-1)
    return
