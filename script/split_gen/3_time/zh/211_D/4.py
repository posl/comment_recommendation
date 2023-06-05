def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)
    return
