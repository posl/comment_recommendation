def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    print(sum(A))

if __name__ == '__main__':
    main()