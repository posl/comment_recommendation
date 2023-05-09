def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for P in permutations(range(1, N)):
        t = T[0][P[0]] + T[P[-1]][0]
        for i in range(N-2):
            t += T[P[i]][P[i+1]]
        if t == K:
            ans += 1
    print(ans)
