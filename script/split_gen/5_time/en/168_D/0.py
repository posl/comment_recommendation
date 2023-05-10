def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("Yes")
    for i in range(1, N + 1):
        print(i - 1 if i % 2 == 0 else i + 1)
