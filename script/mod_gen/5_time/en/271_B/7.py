def main():
    N, Q = map(int, input().split())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split()))[1:])
    for i in range(Q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

if __name__ == '__main__':
    main()