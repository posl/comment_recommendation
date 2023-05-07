def main():
    N, Q = map(int, input().split())
    L = []
    L.append(0)
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s][t])

if __name__ == '__main__':
    main()