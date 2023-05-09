def main():
    import sys
    input = sys.stdin.readline
    import itertools
    N,K = map(int,input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for p in itertools.permutations(range(2,N+1),N-1):
        t = 0
        s = 1
        for i in p:
            t += T[s-1][i-1]
            s = i
        t += T[s-1][0]
        if t == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()