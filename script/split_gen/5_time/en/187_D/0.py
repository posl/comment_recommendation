def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    aoki = sum(A)
    takahashi = 0
    for i in range(N):
        aoki -= A[i]
        takahashi += A[i] + B[i]
        if takahashi > aoki:
            return i + 1
    return N
print(solve())
