def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    pos = dict()
    for i in range(N):
        pos[A[i] * 1000000001 + B[i]] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if i * 1000000001 + j not in pos:
                print(i, j)
