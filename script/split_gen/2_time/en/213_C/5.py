def main():
    H, W, N = map(int, raw_input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, raw_input().split())
    A = map(lambda x: x - 1, A)
    B = map(lambda x: x - 1, B)
    A = sorted(range(N), key=lambda x: A[x])
    B = sorted(range(N), key=lambda x: B[x])
    for i in range(N):
        print A[i] + 1, B[i] + 1
