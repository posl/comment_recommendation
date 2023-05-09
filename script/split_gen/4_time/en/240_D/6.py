def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] - 1
    C = [0 for i in range(N)]
    for i in range(N):
        C[B[i]] += 1
    for i in range(N):
        print(C[i])
