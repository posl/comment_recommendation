Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for m in range(n):
                    for o in range(n):
                        for p in range(n):
                            for q in range(n):
                                for r in range(n):
                                    for s in range(n):
                                        for t in range(n):
                                            for u in range(n):
                                                for v in range(n):
                                                    for w in range(n):
                                                        for x in range(n):
                                                            for y in range(n):
                                                                for z in range(n):
                                                                    for a in range(n):
                                                                        for b in range(n):
                                                                            for c in range(n):
                                                                                for d in range(n):
                                                                                    for e in range(n):
                                                                                        for f in range(n):
                                                                                            for g in range(n):
                                                                                                for h in range(n):
                                                                                                    for i in range(n):
                                                                                                        for j in range(n):
                                                                                                            for l in range(n):
                                                                                                                for m in range(n):
                                                                                                                    for o in range(n):
                                                                                                                        for p in range(n):
                                                                                                                            for q in range(n):
                                                                                                                                for r in range(n):
                                                                                                                                    for s in range(n):
                                                                                                                                        for t in range(n):
                                                                                                                                            for u in range(n):
                                                                                                                                                for v in range(n):
                                                                                                                                                    for w in range(n):
                                                                                                                                                        for x in range(n):
                                                                                                                                                            for y in range(n):
                                                                                                                                                                for z in range(n):
                                                                                                                                                                    for a in range(n):
                                                                                                                                                                        for b in range(n):
                                                                                                                                                                            for c in range(n):
                                                                                                                                                                                for d in range(n):
                                                                                                                                                                                    for e in range(n):
                                                                                                                                                                                        for f in range(n):
                                                                                                                                                                                            for g in range(n):
                                                                                                                                                                                                for h in range(n):
                                                                                                                                                                                                    for i in range(n):
                                                                                                                                                                                                        for j in range(n):
                                                                                                                                                                                                            for l in range(n):
                                                                                                                                                                                                                for m in range(n):
                                                                                                                                                                                                                    for o in range(n):
                                                                                                                                                                                                                        for p in range(n):
                                                                                                                                                                                                                            for q in range(n):
                                                                                                                                                                                                                                for r in range(n):
                                                                                                                                                                                                                                    for s in range(n):
                                                                                                                                                                                                                                        for t in range(n):
                                                                                                                                                                                                                                            for u in range(n):
                                                                                                                                                                                                                                                for v in range(n):

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, K, T))

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        for n in range(m + 1, N):
                            if T[0][i] + T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][0] == K:
                                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for i in range(N)]

    ans = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            if T[i][j] + T[j][i] > K:
                ans += 1

    print(ans * 2)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += T[0][i]
    ans += T[0][N - 1]
    if ans == K:
        ans = 1
    else:
        ans = 0
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    def dfs(v, c):
        if len(c) == N:
            return 1 if v == 0 and sum(c) == K else 0
        return sum(dfs(i, c + [T[v][i]]) for i in range(N) if i not in c)

    print(dfs(0, []))

=======
Suggestion 9

def solve(N,K,T):
    import itertools
    ans = 0
    for p in itertools.permutations(range(1,N)):
        t = 0
        t += T[0][p[0]]
        for i in range(1,N-1):
            t += T[p[i-1]][p[i]]
        t += T[p[N-2]][0]
        if t == K:
            ans += 1
    return ans

N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]
print(solve(N,K,T))
