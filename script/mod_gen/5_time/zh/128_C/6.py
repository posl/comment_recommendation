def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
    for i in range(M):
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    print(N, M)
    print(k)
    print(s)
    print(p)
    return 0

if __name__ == '__main__':
    main()