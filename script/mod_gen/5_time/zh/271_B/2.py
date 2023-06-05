def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(L)
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

if __name__ == '__main__':
    main()