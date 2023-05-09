def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    for i in range(M):
        if i == 0:
            N -= A[i]
        else:
            N -= (A[i] - B[i-1])
        if N <= 0:
            print("No")
            return
        N += (B[i] - A[i])
        if N > T - A[i]:
            N = T - A[i]
    #print(N)
    if N > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()