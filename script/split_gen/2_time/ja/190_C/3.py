def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    # ボールを置いた皿を記録
    # 1-indexed
    balls = [0] * (N + 1)
    ans = 0
    # 全てのパターンを試す
    for i in range(2 ** K):
        # ボールを置く
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        # 条件を満たすか判定
        count = 0
        for a, b in AB:
            if balls[a] and balls[b]:
                count += 1
        ans = max(ans, count)
        # ボールを取り除く
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] -= 1
            else:
                balls[CD[j][1]] -= 1
    print(ans)
