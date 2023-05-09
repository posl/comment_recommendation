def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for j in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])

if __name__ == '__main__':
    main()