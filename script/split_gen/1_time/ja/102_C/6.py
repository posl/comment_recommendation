def main():
    N = int(input())
    A = list(map(int, input().split()))
    # b=0 として、すぬけ君の悲しさの値を計算する
    b = 0
    sadness = 0
    for i in range(N):
        sadness += abs(A[i] - (b + i + 1))
    # 悲しさの値の最小値を求める
    min_sadness = sadness
    for i in range(N - 1):
        # b を 1 ずつ増やしていく
        b += 1
        # b を 1 ずつ増やしていったときの、すぬけ君の悲しさの値を計算する
        sadness -= abs(A[i] - (b + i))
        sadness += abs(A[i + 1] - (b + i + 1))
        # 悲しさの値の最小値を更新する
        if sadness < min_sadness:
            min_sadness = sadness
    print(min_sadness)
