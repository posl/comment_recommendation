def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    # 順列の全探索
    import itertools
    ans = 0
    for p in itertools.permutations(range(1, N)):
        t = T[0][p[0]]
        for i in range(N-2):
            t += T[p[i]][p[i+1]]
        t += T[p[-1]][0]
        if t == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()