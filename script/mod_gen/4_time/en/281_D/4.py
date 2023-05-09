def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if N < K or D == 1:
        print(-1)
        return
    if K == 1:
        print(A[0])
        return
    if N == K:
        print(sum(A))
        return
    if K == 2:
        for i in range(N):
            for j in range(i+1, N):
                if (A[i] + A[j]) % D == 0:
                    print(A[i] + A[j])
                    return
        print(-1)
        return
    if K == 3:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if (A[i] + A[j] + A[k]) % D == 0:
                        print(A[i] + A[j] + A[k])
                        return
        print(-1)
        return
    if K == 4:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        if (A[i] + A[j] + A[k] + A[l]) % D == 0:
                            print(A[i] + A[j] + A[k] + A[l])
                            return
        print(-1)
        return
    if K == 5:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            if (A[i] + A[j] + A[k] + A[l] + A[m]) % D == 0:
                                print(A[i] + A[j] + A[k] + A[l] + A[m])
                                return
        print(-1)
        return
    if K == 6:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            for

if __name__ == '__main__':
    main()