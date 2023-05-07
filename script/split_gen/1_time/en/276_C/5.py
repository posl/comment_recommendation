def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(1, N + 1):
        Q[P[i - 1] - 1] = i
    for i in range(N - 1):
        print(Q[i], end=' ')
    print(Q[N - 1])
