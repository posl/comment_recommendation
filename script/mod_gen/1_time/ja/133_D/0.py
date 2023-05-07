def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = sum(A)
    for i in range(1, N):
        B[i] = A[i-1] - B[i-1] // 2
    print(*B)

if __name__ == '__main__':
    main()