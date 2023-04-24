Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j == k:
                    continue
                if T[i][j] + T[j][k] == K:
                    ans += 1
    print(ans // 2)

=======
Suggestion 2

def main():
    from itertools import permutations
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        t = 0
        t += T[0][p[0]]
        for i in range(N-2):
            t += T[p[i]][p[i+1]]
        t += T[p[N-2]][0]
        if t == K:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        t = T[0][p[0]] + T[p[-1]][0]
        for i in range(N - 2):
            t += T[p[i]][p[i + 1]]
        if t == K:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for i in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                for l in range(N):
                    if l == i or l == j or l == k:
                        continue
                    for m in range(N):
                        if m == i or m == j or m == k or m == l:
                            continue
                        for n in range(N):
                            if n == i or n == j or n == k or n == l or n == m:
                                continue
                            for o in range(N):
                                if o == i or o == j or o == k or o == l or o == m or o == n:
                                    continue
                                for p in range(N):
                                    if p == i or p == j or p == k or p == l or p == m or p == n or p == o:
                                        continue
                                    if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] == K:
                                        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(1, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for m in range(l+1, N):
                        for n in range(m+1, N):
                            for o in range(n+1, N):
                                ans += (T[0][i] + T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][0] == K)

    print(ans)

=======
Suggestion 6

def main():
    N,K=map(int,input().split())
    T=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    for i in range(N):
        for j in range(N):
            if T[i][j]==0:
                T[i][j]=10**9+1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                T[j][k]=min(T[j][k],T[j][i]+T[i][k])
    for

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    # 入力
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))

    # 組み合わせ全探索
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    for m in range(N):
                        for n in range(N):
                            for o in range(N):
                                for p in range(N):
                                    if i == j or i == k or i == l or i == m or i == n or i == o or i == p:
                                        continue
                                    if j == k or j == l or j == m or j == n or j == o or j == p:
                                        continue
                                    if k == l or k == m or k == n or k == o or k == p:
                                        continue
                                    if l == m or l == n or l == o or l == p:
                                        continue
                                    if m == n or m == o or m == p:
                                        continue
                                    if n == o or n == p:
                                        continue
                                    if o == p:
                                        continue

                                    if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] == K:
                                        ans += 1

    # 出力
    print(ans)

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    t = [0]*n
    for i in range(n):
        t[i] = list(map(int, input().split()))

    #全ての経路を列挙
    all_path = []
    for i in range(2, n+1):
        all_path += list(itertools.permutations(range(1, n), i))

    #全ての経路の移動時間の合計を計算
    sum_time = []
    for path in all_path:
        time = 0
        time += t[0][path[0]]
        for i in range(n-2):
            time += t[path[i]][path[i+1]]
        time += t[path[-1]][0]
        sum_time.append(time)

    #移動時間の合計がkになる経路の数を出力
    print(sum_time.count(k))
