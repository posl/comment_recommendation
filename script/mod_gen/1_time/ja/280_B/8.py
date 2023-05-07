def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    A = [0] * N
    for i in range(N):
        A[i] = S[i] - sum(A)
    print(' '.join(str(i) for i in A))

if __name__ == '__main__':
    main()