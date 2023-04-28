Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    rank = [0] * N
    for i in range(N):
        rank[i] = sum(P[i])
    rank.sort(reverse=True)
    for i in range(N):
        if rank[i] >= rank[K-1]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [sum(p) for p in P]
    P.sort(reverse=True)
    print('Yes' if P[K-1] != P[K] else 'No')

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    R = []
    for p in P:
        R.append(sum(p))
    R.sort(reverse=True)
    print("Yes" if R[K-1] > R[K] else "No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if i < K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort(key=lambda x: x[2], reverse=True)
    points.sort(key=lambda x: x[1], reverse=True)
    points.sort(key=lambda x: x[0], reverse=True)
    for i in range(n):
        if points[i][0] == points[k-1][0] and points[i][1] == points[k-1][1] and points[i][2] == points[k-1][2]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(n):
        ans.append('Yes' if sum(p[i]) >= 300 * 3 - (n - k) else 'No')
    print(*ans, sep='\n')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        P[i].append(P[i][0]+P[i][1]+P[i][2])
        ans.append(P[i][3])
    ans.sort(reverse=True)
    print("Yes" if ans.index(P[K-1][3]) < K else "No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    S = [sum(p) for p in P]
    ans = [0]*N
    for i in range(N):
        ans[i] = sum([1 for s in S if S[i] < s])+1
    for a in ans:
        if a <= K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 3日間の合計点を計算
    S = [sum(p) for p in P]

    # 4日目の点数を計算
    Q = [S[i] + 300 for i in range(N)]

    # 4日目の点数でソート
    Q.sort(reverse=True)

    # K位以内に入っているかどうか判定
    for i in range(N):
        if Q.index(S[i] + 300) < K:
            print('Yes')
        else:
            print('No')
