def main():
    import itertools
    N,K = map(int,input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in itertools.permutations(range(1,N)):
        t = 0
        for j in range(N-1):
            t += T[i[j]][i[j+1]]
        t += T[0][i[0]] + T[i[-1]][0]
        if t == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()