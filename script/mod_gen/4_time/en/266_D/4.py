def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    max_size = 0
    for i in range(N):
        if i == 0:
            max_size = A[i]
        else:
            max_size = max(max_size, A[i] + A[i - 1] - abs(X[i] - X[i - 1]) - (T[i] - T[i - 1]))
    print(max_size)

if __name__ == '__main__':
    solve()