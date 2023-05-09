def main():
    N, K = map(int, input().split())
    t = [0] * N
    d = [0] * N
    for i in range(N):
        t[i], d[i] = map(int, input().split())
    # おいしさが高い順にソート
    order = sorted(range(N), key=lambda x: d[x], reverse=True)
    # 選んだ寿司のネタ
    s = set()
    # 種類ボーナスポイント
    x = 0
    # おいしさ基礎ポイント
    y = 0
    # 選んだ寿司の種類数
    count = 0
    for i in range(K):
        if t[order[i]] not in s:
            count += 1
            s.add(t[order[i]])
        y += d[order[i]]
    x = count * count
    ans = y + x
    for i in range(K, N):
        if t[order[i]] in s:
            continue
        # 種類ボーナスポイントは最大でも K * K
        if x + 2 * count + 1 > K * K:
            break
        count += 1
        s.add(t[order[i]])
        y += d[order[i]]
        x += 2 * count + 1
        ans = max(ans, y + x)
    print(ans)
