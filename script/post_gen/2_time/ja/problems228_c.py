Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [0] * N
    for i in range(N):
        P[i] = sum(map(int, input().split()))
    P.sort(reverse=True)
    if P[K - 1] < P[K]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        if sum(p[i]) + 300 * (3 - len(p[i])) >= sum(sorted([sum(p[j]) for j in range(n) if i != j])[-k:]):
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        p = list(map(int, input().split()))
        P.append(p)
    for i in range(N):
        rank = 1
        for j in range(N):
            if P[i][0] + P[i][1] + P[i][2] < P[j][0] + P[j][1] + P[j][2]:
                rank += 1
        if rank <= K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        x = 0
        for j in range(N):
            if sum(A[i]) < sum(A[j]):
                x += 1
        if x < K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = sorted(P, key=lambda x: sum(x), reverse=True)
    print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] >= P[K][0] + P[K][1] + P[K][2] else 'No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 各生徒の合計点を求める
    S = [sum(p) for p in P]

    # 合計点の降順にソートしたインデックスを求める
    # 例えば、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、[0, 1, 2, 3, 4] の順でソートされている
    # これを、[0, 1, 2, 3, 4] というインデックスでソートする
    # つまり、[0, 1, 2, 3, 4] の順でソートされている
    # つまり、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、S = [5, 4, 3, 2, 1] の場合、
    # [0, 1, 2, 3, 4] となる
    # つまり、

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    # 入力を受け取る
    P = [list(map(int, input().split())) for _ in range(N)]

    # 3 日目の合計点のリストを作る
    S = [sum(p) for p in P]

    # 4 日目の試験後の順位を計算する
    # 4 日目の試験後の順位は、その生徒よりも 4 日間の合計点が高い生徒の人数に 1 を加えた値として定めます。
    R = [sum(s > t for t in S) + 1 for s in S]

    # 上位 K 位以内に入っていることがあり得るかどうか判定して出力する
    for r in R:
        print('Yes' if r <= K else 'No')

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 3日目までの合計点
    S = [p[0] + p[1] + p[2] for p in P]

    # 4日目の得点
    T = [300 - p[3] for p in P]

    # 4日目の得点でソート
    T_sorted = sorted(T)

    # 4日目の得点でソートしたときの順位
    rank = [0] * N
    for i, t in enumerate(T_sorted):
        rank[T.index(t)] = i + 1

    # 3日目までの合計点でソート
    S_sorted = sorted(S)

    # 4日目の得点でソートしたときの順位と、3日目までの合計点でソートしたときの順位の差がK以下であればYes
    for i in range(N):
        if rank[i] - S_sorted.index(S[i]) <= K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]

    # 3日目までの合計点
    score = [sum(p[i]) for i in range(n)]

    # 4日目の試験の点数の上位k人の合計点
    score.sort(reverse=True)
    top = sum(score[:k])

    for i in range(n):
        # 4日目の試験で最大の合計点を取れる場合
        if score[k-1] + p[i][3] >= top:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 3日目の合計点を計算
    sum3 = [sum(p) for p in P]
    # 4日目の合計点の上位 K 位までを求める
    sum4 = sorted([sum(p) for p in P], reverse=True)[:K]
    for i in range(N):
        # 4日目の合計点が上位 K 位に入る場合
        if sum3[i] + 300 in sum4:
            print("Yes")
        # 4日目の合計点が上位 K 位に入らない場合
        else:
            # 3日目の合計点が上位 K 位に入る場合
            if sum3[i] in sum4:
                # 3日目の合計点が上位 K 位に入るが、4日目の合計点が上位 K 位に入らない場合
                if sum3[i] + 300 not in sum4:
                    print("Yes")
                # 3日目の合計点が上位 K 位に入るが、4日目の合計点が上位 K 位に入る場合
                else:
                    print("No")
            # 3日目の合計点が上位 K 位に入らない場合
            else:
                print("No")
