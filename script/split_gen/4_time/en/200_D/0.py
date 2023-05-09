def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] % 200
        C[i] = i + 1
    print("Yes")
    print(N)
    print(*C)
    print(N)
    print(*B)
