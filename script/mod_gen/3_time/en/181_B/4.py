def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    sum = 0
    for i in range(N):
        sum += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2
    print(sum % 1000000007)

if __name__ == '__main__':
    main()