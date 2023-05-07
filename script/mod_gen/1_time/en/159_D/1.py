def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_count = [0] * (N + 1)
    for i in range(N):
        A_count[A[i]] += 1
    total = 0
    for i in range(1, N + 1):
        total += A_count[i] * (A_count[i] - 1) // 2
    for i in range(N):
        print(total - (A_count[A[i]] - 1))

if __name__ == '__main__':
    main()