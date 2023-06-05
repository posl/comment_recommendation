def swap(a, b):
    return b, a
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
for i in range(P-1, Q):
    A[i], A[i+R-Q] = swap(A[i], A[i+R-Q])
print(' '.join(map(str, A)))

if __name__ == '__main__':
    swap()