def main():
    # input
    N = int(input())
    S = list(map(int, input().split()))
    # compute
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    # output
    print(*A)

if __name__ == '__main__':
    main()