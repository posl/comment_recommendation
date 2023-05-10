def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    for i in range(Q):
        count = 0
        for j in range(N):
            count += abs(A[j] - X[i])
        print(count)
