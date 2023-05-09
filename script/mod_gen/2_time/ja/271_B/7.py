def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)
    B = []
    for i in range(N):
        for j in range(1, A[i][0]+1):
            B.append(A[i][j])
    #print(B)
    for _ in range(Q):
        s, t = map(int, input().split())
        print(B[s+t-2])

if __name__ == '__main__':
    main()