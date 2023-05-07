def main():
    N, W = map(int, input().split())
    # 時間ごとの使用量を記録する配列を用意
    water = [0] * 200005
    # 各人の使用量を記録
    for i in range(N):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    # 時間ごとに使用量を計算
    for i in range(200005):
        if i == 0:
            continue
        water[i] += water[i - 1]
        if water[i] > W:
            print('No')
            return
    print('Yes')
