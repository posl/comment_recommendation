def main():
    import sys
    from itertools import combinations
    input = sys.stdin.readline
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = -10**18
    for i in range(2**3):
        tmp = []
        for j in range(N):
            tmp.append(sum([(-1)**((i>>k)&1)*xyz[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
