def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    # 答え
    ans = 0
    # キャンディの種類を数える
    cnt = [0] * (10 ** 9 + 1)
    # 種類数
    kind = 0
    # K個のキャンディの中の種類数を数える
    for i in range(K):
        if cnt[c[i]] == 0:
            kind += 1
        cnt[c[i]] += 1
    # K個のキャンディの中の種類数を更新
    for i in range(K, N):
        if cnt[c[i - K]] == 1:
            kind -= 1
        cnt[c[i - K]] -= 1
        if cnt[c[i]] == 0:
            kind += 1
        cnt[c[i]] += 1
        ans = max(ans, kind)
    print(ans)
    return
