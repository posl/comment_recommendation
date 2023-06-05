def main():
    N = int(input())
    T = [0] * (N + 1)
    X = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], X[i], A[i] = map(int, input().split())
    T[0] = 0
    X[0] = 0
    A[0] = 0
    maxA = [0] * (N + 1)
    for i in range(1, N + 1):
        maxA[i] = max(maxA[i - 1], A[i])
    ans = 0
    for i in range(1, N + 1):
        if (T[i] - T[i - 1]) >= abs(X[i] - X[i - 1]):
            if ((T[i] - T[i - 1]) - abs(X[i] - X[i - 1])) % 2 == 0:
                ans = max(ans, maxA[i])
            else:
                ans = max(ans, maxA[i - 1], maxA[i])
        else:
            ans = max(ans, maxA[i - 1], maxA[i])
    print(ans)
