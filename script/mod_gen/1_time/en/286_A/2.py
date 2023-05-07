def swap(A, P, Q, R, S):
    B = []
    B.extend(A[0:P-1])
    B.extend(A[R-1:S])
    B.extend(A[Q:S])
    B.extend(A[P-1:Q-1])
    B.extend(A[S:])
    return B
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap(A, P, Q, R, S)
print(' '.join(map(str, B)))

if __name__ == '__main__':
    swap()