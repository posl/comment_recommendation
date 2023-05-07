def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** N):
        c = 1
        for j in range(N):
            if (i >> j) & 1:
                c *= L[j][(i >> j) & 1]
        if c == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()