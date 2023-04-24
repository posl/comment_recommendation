Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    score = sum(P[K - 1])
    count = 0
    for i in range(N):
        if score < sum(P[i]):
            count += 1
    if count < K:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0]+x[1]+x[2], reverse=True)
    #print(P)
    #print(P[K-1][0]+P[K-1][1]+P[K-1][2])
    for i in range(N):
        if P[i][0]+P[i][1]+P[i][2] >= P[K-1][0]+P[K-1][1]+P[K-1][2]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = sorted(P, key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print(P[K-1][0] + P[K-1][1] + P[K-1][2])
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] >= P[K-1][0] + P[K-1][1] + P[K-1][2]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [sum(p) for p in P]
    P.sort(reverse=True)
    for i in range(N):
        if P[i] < P[K-1]:
            print("No")
        else:
            print("Yes")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    s = [sum(p[i]) for i in range(n)]
    for i in range(n):
        s[i] += 300 * (k - 1)
        if s[i] > sum(p[i]) + 300 * (k - 1):
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    Q = [sorted(P[i], reverse=True) for i in range(N)]
    R = [sum(Q[i][:3]) for i in range(N)]
    S = sorted(R, reverse=True)
    T = [S.index(R[i]) + 1 for i in range(N)]
    for i in range(N):
        if T[i] <= K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) + (3 * (K - 1)) >= sum(P[K - 1]):
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    #各生徒の合計点を求める
    #N個の要素を持つ配列を用意
    total = [0] * N
    for i in range(N):
        total[i] = sum(P[i])

    #合計点をソートする
    total.sort()

    #各生徒の合計点が、全体の合計点のうち上位K人に入っているかどうかを判定する
    for i in range(N):
        if sum(P[i]) >= total[-K]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    p = [list(map(int,input().split())) for i in range(n)]
    p = sorted(p,key=lambda x:sum(x),reverse=True)
    for i in range(n):
        if p[i][0]+p[i][1]+p[i][2] < p[k-1][0]+p[k-1][1]+p[k-1][2]:
            print("No")
        else:
            print("Yes")

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    # 3日目の合計点を計算
    points3 = [sum(map(int, input().split())) for _ in range(N)]
    # 4日目の合計点を計算
    points4 = [p + int(input()) for p in points3]
    # 3日目の合計点を降順にソート
    points3.sort(reverse=True)
    # 3日目の上位K人の合計点を求める
    top3 = points3[K - 1]
    # 4日目の合計点を降順にソート
    points4.sort(reverse=True)
    # 4日目の上位K人の合計点を求める
    top4 = points4[K - 1]
    # 3日目の上位K人の合計点が4日目の上位K人の合計点以上の場合は、
    # 4日目に全員が300点を取れば、4日目の上位K人の合計点は4日目の上位K人の合計点以上になる
    if top3 >= top4:
        print('Yes')
    else:
        print('No')
