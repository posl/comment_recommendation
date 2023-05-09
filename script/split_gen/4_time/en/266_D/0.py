def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        if i == 0:
            if X[i] <= T[i]:
                ans += A[i]
        else:
            if X[i] - X[i - 1] <= T[i] - T[i - 1]:
                ans += A[i]
    print(ans)
