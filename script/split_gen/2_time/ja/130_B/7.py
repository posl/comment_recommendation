def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    # 座標を格納するリスト
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    # 答えを格納する変数
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1
    print(ans)
