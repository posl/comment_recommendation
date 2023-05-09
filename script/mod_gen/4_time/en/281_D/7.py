def problem():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if K > N:
        return -1
    if K == 1:
        if A[0] % D == 0:
            return A[0]
        else:
            return -1
    if K == 2:
        for i in range(N-1):
            if (A[i] + A[i+1]) % D == 0:
                return A[i] + A[i+1]
        return -1
    if K == 3:
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if (A[i] + A[j] + A[k]) % D == 0:
                        return A[i] + A[j] + A[k]
        return -1
    if K == 4:
        for i in range(N-3):
            for j in range(i+1, N-2):
                for k in range(j+1, N-1):
                    for l in range(k+1, N):
                        if (A[i] + A[j] + A[k] + A[l]) % D == 0:
                            return A[i] + A[j] + A[k] + A[l]
        return -1
    if K == 5:
        for i in range(N-4):
            for j in range(i+1, N-3):
                for k in range(j+1, N-2):
                    for l in range(k+1, N-1):
                        for m in range(l+1, N):
                            if (A[i] + A[j] + A[k] + A[l] + A[m]) % D == 0:
                                return A[i] + A[j] + A[k] + A[l] + A[m]
        return -1
    if K == 6:
        for i in range(N-5):
            for j in range(i+1, N-4):
                for k in range(j+1, N-3):
                    for l in range(k+1, N-2):
                        for m in range(l+1, N-1):
                            for n in range(m+1

if __name__ == '__main__':
    problem()