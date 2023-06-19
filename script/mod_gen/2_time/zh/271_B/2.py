def main():
    n,q = map(int,input().split())
    L = []
    for i in range(n):
        L.append(list(map(int,input().split())))
    S = []
    for i in range(q):
        S.append(list(map(int,input().split())))
    for i in range(q):
        print(L[S[i][0]-1][S[i][1]-1])

if __name__ == '__main__':
    main()