def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    path = [0] * N
    for i in range(M):
        path[A[i] - 1] += 1
        path[B[i] - 1] += 1
    if max(path) == 2:
        print("Yes")
    else:
        print("No")
