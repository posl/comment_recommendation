def main():
    N = int(input())
    A = list(map(int, input().split()))
    # b = 0 とする
    b = 0
    # すぬけ君の悲しさの値を計算
    sadness = 0
    for i in range(N):
        sadness += abs(A[i] - (b + i + 1))
    # b = 1 ~ N として、すぬけ君の悲しさの値を計算し、最小値を求める
    for i in range(1, N):
        # すぬけ君の悲しさの値を計算
        sadness_tmp = 0
        for j in range(N):
            sadness_tmp += abs(A[j] - (i + j + 1))
        # すぬけ君の悲しさの値が最小値なら更新
        if sadness_tmp < sadness:
            sadness = sadness_tmp
    print(sadness)
