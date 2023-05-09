def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    S = []
    for i in range(Q):
        S.append(list(map(int, input().split())))
    for i in range(Q):
        print(A[S[i][0]-1][S[i][1]-1])

if __name__ == '__main__':
    main()