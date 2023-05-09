def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    pos = [[0] * 2 for _ in range(N + 1)]
    for i in range(N):
        pos[A[i]][0] = i + 1
        pos[B[i]][1] = i + 1
    pos.sort()
    num = [0] * N
    for i in range(N):
        num[pos[i][0]] = i + 1
    for i in range(1, N + 1):
        num[i] += num[i - 1]
    for i in range(N):
        print(num[A[i]], num[B[i]])
