def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(AB)
    A = [0] * N
    B = [0] * N
    for i in range(M):
        A[AB[i][0] - 1] += 1
        B[AB[i][1] - 1] += 1
    #print(A)
    #print(B)
    for i in range(N):
        print(A[i] + B[i])
main()

if __name__ == '__main__':
    main()