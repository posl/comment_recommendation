def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = (A[0] + A[1] - A[-1]) // 2
    for i in range(1, N):
        B[i] = A[i-1] - B[i-1]
    print(*B)
main()
