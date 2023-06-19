def main():
    # input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # compute
    B = [0]*N
    for i in A:
        B[i-1] = 1
    for i in L:
        if B[A[i-1]-1] == 1:
            if A[i-1] < N:
                if B[A[i-1]] == 0:
                    B[A[i-1]-1] = 0
                    B[A[i-1]] = 1
                    A[i-1] += 1
            else:
                B[A[i-1]-1] = 0
                B[0] = 1
                A[i-1] = 1
    # output
    for i in range(N):
        if B[i] == 1:
            print(i+1, end=' ')
main()
