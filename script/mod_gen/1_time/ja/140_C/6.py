def main():
    N = int(input())
    B = [int(x) for x in input().split()]
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

if __name__ == '__main__':
    main()