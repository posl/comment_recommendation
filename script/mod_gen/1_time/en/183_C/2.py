def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        time = 0
        now = 0
        for i in p:
            time += T[now][i]
            now = i
        time += T[now][0]
        if time == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()