def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    # ボールの数を数える
    balls = [0] * N
    for c, d in CD:
        balls[c - 1] += 1
        balls[d - 1] += 1
    # 条件を満たすかどうかを調べる
    ans = 0
    for a, b in AB:
        if balls[a - 1] >= 1 and balls[b - 1] >= 1:
            ans += 1
    # 出力
    print(ans)
