def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    par = [i for i in range(N+1)]
    rank = [0 for i in range(N+1)]
    for i in range(1, M):
        a, b = AB[i]
        ans[i] = ans[i-1] - union(a, b, par, rank)
    ans.reverse()
    for i in ans:
        print(i)
