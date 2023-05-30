def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0 and A[-1] < 0:
        if K <= ((N*(N-1))//2):
            return A[K-1]
        else:
            return A[0] * A[-1] // A[K-N*(N-1)//2-1]
    elif A[0] < 0 and A[-1] >= 0:
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N-i-1
            else:
                break
        if K <= cnt:
            return A[K-1]
        elif K > ((N*(N-1))//2 - cnt):
            return A[0] * A[-1] // A[K-N*(N-1)//2+cnt-1]
        else:
            return A[0] * A[-1] // A[cnt+K-1]
    else:
        if K <= ((N*(N-1))//2):
            return A[K-1]
        else:
            return A[0] * A[-1] // A[K-N*(N-1)//2-1]
print(solve())
