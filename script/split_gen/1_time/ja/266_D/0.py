def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    # print(T)
    # print(X)
    # print(A)
    # すぬけ君がいる穴のリストを作成
    holes = [[] for _ in range(5)]
    for i in range(N):
        holes[X[i]].append([T[i], A[i]])
    # print(holes)
    # すぬけ君がいる穴のリストをソート
    for i in range(5):
        holes[i].sort()
    # print(holes)
    # すぬけ君を捕まえるのにかかる時間を計算
    # 捕まえるのにかかる時間は無視できるので、
    # すぬけ君がいる穴のリストの長さの最大値を求める
    max_len = 0
    for i in range(5):
        if len(holes[i]) > max_len:
            max_len = len(holes[i])
    # print(max_len)
    # 捕まえるのにかかる時間の最大値を求める
    ans = 0
    for i in range(max_len):
        sum_A = 0
        for j in range(5):
            if i < len(holes[j]):
                sum_A += holes[j][i][1]
        if sum_A > ans:
            ans = sum_A
    print(ans)
