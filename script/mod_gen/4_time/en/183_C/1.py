def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(2, N+1)):
        t = T[0][p[0]-1]
        for i in range(N-2):
            t += T[p[i]-1][p[i+1]-1]
        t += T[p[-1]-1][0]
        if t == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()