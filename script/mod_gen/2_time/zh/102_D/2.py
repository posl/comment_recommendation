def get_min_max_diff(A):
    N = len(A)
    min_diff = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                P = sum(A[:i])
                Q = sum(A[i:j])
                R = sum(A[j:k])
                S = sum(A[k:])
                diff = max(P, Q, R, S) - min(P, Q, R, S)
                if diff < min_diff:
                    min_diff = diff
    return min_diff

if __name__ == '__main__':
    get_min_max_diff()