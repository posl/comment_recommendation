def main():
    import sys
    from itertools import permutations
    def input():
        return sys.stdin.readline()[:-1]
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for p in permutations(range(1, n)):
        time = t[0][p[0]] + t[p[-1]][0]
        for i in range(n-2):
            time += t[p[i]][p[i+1]]
        if time == k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()