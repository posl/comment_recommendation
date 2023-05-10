def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    X = [0] * N
    for a in A:
        X[a - 1] += 1
    for x in X:
        if K - Q + x > 0:
            print("Yes")
        else:
            print("No")
