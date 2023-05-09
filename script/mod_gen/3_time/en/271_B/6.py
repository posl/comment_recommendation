def main():
    N,Q = map(int,input().split())
    L = [list(map(int,input().split())) for i in range(N)]
    S = [list(map(int,input().split())) for i in range(Q)]
    for i in range(Q):
        print(L[S[i][0]-1][S[i][1]])

if __name__ == '__main__':
    main()