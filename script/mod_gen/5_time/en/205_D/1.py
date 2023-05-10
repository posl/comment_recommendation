def main():
    # input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # compute
    A.sort()
    #print(A)
    B = [0] + [A[i] - A[i-1] - 1 for i in range(1, N)]
    #print(B)
    C = [0] + [B[i] + C[i-1] for i in range(1, N)]
    #print(C)
    # output
    for k in K:
        if k <= C[-1]:
            for i in range(1, N):
                if k <= C[i]:
                    print(A[i-1] + k - C[i-1])
                    break
        else:
            print(A[-1] + k - C[-1])

if __name__ == '__main__':
    main()