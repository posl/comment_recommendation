def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(A[-K])
        else:
            print(A[K-1])
        return
    if K % 2 == 0:
        K = K // 2
        ans = 1
        for i in range(N):
            if A[i] <= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        ans = 1
        for i in range(N-1, -1, -1):
            if A[i] >= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        print(A[K-1])
        return
    else:
        ans = 1
        for i in range(N):
            if A[i] <= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        ans = 1
        for i in range(N-1, -1, -1):
            if A[i] >= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        print(A[K-1])
        return
