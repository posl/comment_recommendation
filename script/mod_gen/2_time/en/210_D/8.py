def main():
    from sys import stdin
    import numpy as np
    H, W, C = map(int, stdin.readline().split())
    A = np.array([list(map(int, stdin.readline().split())) for i in range(H)])
    B = np.array([list(map(int, stdin.readline().split())) for i in range(H)])
    result = A[0, 0] + B[0, 0] + C * (H + W - 2)
    for i in range(H):
        for j in range(W):
            temp = A[i, j] + B[i, j] + C * (i + j)
            result = min(result, temp)
    for i in range(H):
        for j in range(W):
            temp = A[i, j] + B[i, j] + C * (H - i - 1 + W - j - 1)
            result = min(result, temp)
    print(result)

if __name__ == '__main__':
    main()