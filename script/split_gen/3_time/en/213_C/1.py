def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    h = [0] * (H + 1)
    w = [0] * (W + 1)
    for i in range(N):
        h[A[i]] = 1
        w[B[i]] = 1
    for i in range(1, H + 1):
        h[i] += h[i - 1]
    for i in range(1, W + 1):
        w[i] += w[i - 1]
    for i in range(N):
        print(h[A[i]], w[B[i]])
