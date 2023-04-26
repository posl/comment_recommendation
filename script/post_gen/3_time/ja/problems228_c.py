Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    rank = [1] * N
    for i in range(1, N):
        if P[i - 1][0] + P[i - 1][1] + P[i - 1][2] == P[i][0] + P[i][1] + P[i][2]:
            rank[i] = rank[i - 1]
        else:
            rank[i] = i + 1

    for i in range(N):
        if rank[i] <= K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = [[0, 0, 0, 0] for i in range(N)]
    for i in range(N):
        P[i][0], P[i][1], P[i][2] = map(int, input().split())
        P[i][3] = P[i][0] + P[i][1] + P[i][2]
    P.sort(key=lambda x: x[3], reverse=True)
    for i in range(N):
        if P[i][3] + 300 * (3 - i) < P[K - 1][3]:
            print('No')
        else:
            print('Yes')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: sum(x), reverse=True)
    #print(P)
    for i in range(N):
        if i < K-1:
            print("Yes")
        else:
            if sum(P[i]) < sum(P[K-1]):
                print("No")
            else:
                print("Yes")

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p = [[sum(p[i]), p[i][0]] for i in range(n)]
    p.sort(reverse=True)
    for i in range(n):
        if p[i][1] + p[k-1][0] < p[k-1][0]:
            print('No')
        else:
            print('Yes')

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    S = [sum(p) for p in P]
    rank = [0] * N
    for i in range(N):
        for j in range(N):
            if S[i] < S[j]:
                rank[i] += 1
    for i in range(N):
        if rank[i] <= K-1:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    def check(x):
        cnt = 0
        for i in range(N):
            total = sum(P[i])
            if total + x >= 300 * 3:
                cnt += 1
        return cnt >= K

    ok = 300
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    score = []
    for _ in range(n):
        score.append(sum(map(int, input().split())))
    score.sort(reverse = True)
    for i in range(n):
        if score[i] < score[k - 1]:
            print("No")
        else:
            print("Yes")

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    data = []
    for i in range(N):
        data.append(list(map(int,input().split())))
    data.sort(key=lambda x:sum(x),reverse=True)
    for i in range(N):
        if sum(data[i]) + sum(data[K-1]) < sum(data[K]):
            print('No')
        else:
            print('Yes')

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 点数の合計を求める
    sum_P = [sum(p) for p in P]

    # 点数の合計を降順にソートしたときのインデックスを求める
    sorted_sum_P = sorted(range(N), key=lambda x: sum_P[x], reverse=True)

    # 点数の合計が同じものがあるかどうかをチェック
    same = False
    for i in range(N - 1):
        if sum_P[sorted_sum_P[i]] == sum_P[sorted_sum_P[i + 1]]:
            same = True
            break

    # 点数の合計が同じものがある場合は、
    # その点数の合計を取った人のうち、
    # 3 日目の点数が高い順にソートしたときのインデックスを求める
    if same:
        for i in range(N - 1):
            if sum_P[sorted_sum_P[i]] == sum_P[sorted_sum_P[i + 1]]:
                sorted_P = sorted(range(i, i + 2), key=lambda x: P[x][2], reverse=True)
                sorted_sum_P[i:i + 2] = sorted_P

    # 上位 K 位以内に入っているかどうかをチェック
    for i in range(N):
        if sorted_sum_P.index(i) < K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def solve(n, k, p):
    # 1日目の点数を基準にソート
    p.sort(key=lambda x: x[0], reverse=True)
    # 1日目の点数の順位
    rank = [0] * n
    # 1日目の点数の順位を計算
    for i in range(n):
        if i != 0 and p[i][0] != p[i - 1][0]:
            rank[i] = rank[i - 1] + 1
        else:
            rank[i] = rank[i - 1]
    # 4日目の点数の上位K人の最低点数
    min_4th = p[k - 1][0] + p[k - 1][1] + p[k - 1][2]
    # 3日目までの点数を基準にソート
    p.sort(key=lambda x: x[1] + x[2], reverse=True)
    # 3日目までの点数の順位
    rank3 = [0] * n
    # 3日目までの点数の順位を計算
    for i in range(n):
        if i != 0 and p[i][1] + p[i][2] != p[i - 1][1] + p[i - 1][2]:
            rank3[i] = rank3[i - 1] + 1
        else:
            rank3[i] = rank3[i - 1]
    # 3日目までの点数の順位と1日目の点数の順位を合わせた順位
    rank4 = [0] * n
    for i in range(n):
        rank4[i] = rank[i] + rank3[i]
    # 3日目までの点数の合計がmin_4thを超える場合は4日目の点数で上位K人に入ることができる
    for i in range(n):
        if p[i][1] + p[i][2] >= min_4th:
            print("Yes")
        else:
            # 4
