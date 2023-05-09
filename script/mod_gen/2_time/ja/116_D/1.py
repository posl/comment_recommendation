def main():
    N, K = map(int, input().split())
    t = [0] * N
    d = [0] * N
    for i in range(N):
        t[i], d[i] = map(int, input().split())
    # おいしさの降順にソート
    idx = sorted(range(N), key=lambda x: d[x], reverse=True)
    # 選んだ寿司のネタの種類を管理
    kind = [0] * (N + 1)
    # おいしさの合計
    sum = 0
    # 選んだ寿司のネタの種類数
    k = 0
    # おいしさの合計が最大になるように選ぶ
    for i in range(K):
        sum += d[idx[i]]
        if kind[t[idx[i]]] == 0:
            k += 1
        kind[t[idx[i]]] += 1
    ans = sum + k * k
    # おいしさの合計が最大になるように選んだ寿司のネタを一つ減らす
    for i in range(K):
        if kind[t[idx[i]]] == 1:
            # 選んだ寿司のネタが一つしかない場合は、他の選んでいない寿司を選ぶ
            for j in range(N):
                if kind[t[j]] == 0:
                    sum -= d[idx[i]]
                    sum += d[j]
                    kind[t[idx[i]]] -= 1
                    kind[t[j]] += 1
                    ans = max(ans, sum + k * k)
                    break
        else:
            # 選んだ寿司のネタが二つ以上ある場合は、一番おいしさが低い寿司を選ぶ
            for j in range(i + 1, K):
                if t[idx[i]] == t[idx[j]]:
                    sum -= d[idx[i]]
                    sum += d[idx[j]]
                    kind[t[idx[i]]] -= 1

if __name__ == '__main__':
    main()