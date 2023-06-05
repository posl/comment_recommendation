def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    if A[N-1] == A[N-2]:
        print('No')
        exit()
    if abs(A[N-1]-A[N-2]) > abs(x):
        print('No')
        exit()
    print('Yes')
