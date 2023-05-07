def main():
    N, W = map(int, input().split())
    # お湯を使う時刻と、その時刻に使う量をリストに格納
    use = []
    for i in range(N):
        S, T, P = map(int, input().split())
        use.append([S, P])
        use.append([T, -P])
    # 使う量を時刻順に並び替え
    use.sort()
    # お湯の総量
    total = 0
    # お湯の総量が給湯器の量より多くなった場合、Noを出力
    for i in range(len(use)):
        total += use[i][1]
        if total > W:
            print("No")
            return
    print("Yes")
