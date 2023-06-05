def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += B[A[i] - 1]
        if i < N - 1 and A[i] + 1 == A[i + 1]:
            sum += C[A[i] - 1]
    print(sum)
