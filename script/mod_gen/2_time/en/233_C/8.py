def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    #print(N, X)
    #print(L)
    ans = 0
    for i in range(2**N):
        s = 1
        for j in range(N):
            if ((i >> j) & 1):
                s *= L[j][1]
            else:
                s *= L[j][2]
        if s == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()