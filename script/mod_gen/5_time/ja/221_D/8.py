def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #D = [0] * N
    D = [0 for i in range(N)]
    #print(D)
    for i in range(N):
        for j in range(A[i], A[i]+B[i]):
            if j <= N:
                D[j-1] += 1
    print(*D)

if __name__ == '__main__':
    main()