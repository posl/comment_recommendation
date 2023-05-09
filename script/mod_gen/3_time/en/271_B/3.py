def main():
    N, Q = [int(x) for x in input().split()]
    a = []
    for i in range(N):
        a.append([int(x) for x in input().split()])
    for i in range(Q):
        s, t = [int(x) for x in input().split()]
        print(a[s - 1][t])

if __name__ == '__main__':
    main()