Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2])
    #print(P)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] >= P[K-1][0] + P[K-1][1] + P[K-1][2]:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    sum_ = sum(P[K-1])
    for i in range(K):
        if sum_ < sum(P[i]):
            print("No")
        else:
            print("Yes")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[K - 1][0] + P[K - 1][1] + P[K - 1][2] >= 300 * K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(N):
        if score[i][0] + score[i][1] + score[i][2] + score[K - 1][3] < score[K - 1][0] + score[K - 1][1] + score[K - 1][2] + score[K - 1][3]:
            print("No")
        else:
            print("Yes")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) >= (K-1)*300:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        if (P[i][0] + P[i][1] + P[i][2]) >= (K * 300):
            ans.append("Yes")
        else:
            ans.append("No")
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        if sum(P[i]) >= 100 * K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: -x[0] - x[1] - x[2])
    print("Yes" if p[k - 1][0] + p[k - 1][1] + p[k - 1][2] >= p[k][0] + p[k][1] + p[k][2] else "No")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 1. 点数の計算
    # 2. 降順ソート
    # 3. K番目の人の点数を取得
    # 4. 各人の点数がK番目の点数以上か判定

    # 1. 点数の計算
    # 2. 降順ソート
    # 3. K番目の人の点数を取得
    # 4. 各人の点数がK番目の点数以上か判定
    P = sorted([sum(p) for p in P], reverse=True)
    Kth = P[K-1]

    # 4. 各人の点数がK番目の点数以上か判定
    for p in [sum(p) for p in P]:
        if p >= Kth:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 1日目の得点が300点の場合、最高得点が1200点
    # 2日目の得点が300点の場合、最高得点が1500点
    # 3日目の得点が300点の場合、最高得点が1800点
    # 4日目の得点が300点の場合、最高得点が2100点
    # 4日目の得点が0点の場合、最高得点が1200点
    # 4日目の得点が0点の場合、最高得点が1500点
    # 4日目の得点が0点の場合、最高得点が1800点
    # 4日目の得点が0点の場合、最高得点が1200点
    # 4日目の得点が0点の場合、最高得点が1500点
    # 4日目の得点が0点の場合、最高得点が1800点
    # 4日目の得点が0点の場合、最高得点が1200点
    # 4日目の得点が0点の場合、最高得点が1500点
    # 4日目の得点が0点の場合、最高得点が1800点
    # 4日目の得点が0点の場合、最高得点が1200点
    # 4日目の得点が0点の場合、最高得点が1500点
    # 4日目の得点が0点の場合、最高得点が1800点
    # 4日目の得点が0点の場合、最高得点が1200点
    # 4日目の得点が0点の場合、最高得点が1500点
    # 4日目の得点が0点の場合、最高
