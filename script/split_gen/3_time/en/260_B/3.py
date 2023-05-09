def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(A[i] + B[i], i + 1) for i in range(N)]
    C.sort(reverse=True)
    print(*[C[i][1] for i in range(X + Y + Z)], sep='
')
