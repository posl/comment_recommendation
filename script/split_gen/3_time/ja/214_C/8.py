def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # すぬけ君の宝石を貰う時刻
    # 初期値はT_i
    recieve = T[:]
    # すぬけ君の宝石を渡す時刻
    give = [0] * N
    # すぬけ君の宝石を渡す時刻を計算する
    for i in range(N):
        give[i] = recieve[i] + S[i]
    # すぬけ君の宝石を貰う時刻を計算する
    for i in range(N):
        # すぬけ君の宝石を渡す時刻よりも
        # すぬけ君の宝石を貰う時刻が大きい場合
        if recieve[(i + 1) % N] < give[i]:
            # すぬけ君の宝石を渡す時刻を
            # すぬけ君の宝石を貰う時刻とする
            recieve[(i + 1) % N] = give[i]
    # すぬけ君の宝石を貰う時刻を出力する
    for i in range(N):
        print(recieve[i])
