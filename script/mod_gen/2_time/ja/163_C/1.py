def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    print(*B, sep = '
')
main()
