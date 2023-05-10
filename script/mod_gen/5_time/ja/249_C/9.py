def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 各文字列に含まれる文字の種類数を数える
    cnt = [0] * N
    for i in range(N):
        cnt[i] = len(set(S[i]))
    # すべての組み合わせを試す
    ans = 0
    for i in range(1 << N):
        # 選んだ文字列を入れる
        selected = []
        for j in range(N):
            if (i >> j) & 1:
                selected.append(S[j])
        # 選んだ文字列に含まれる文字の種類数を数える
        num = len(set(''.join(selected)))
        if num == K:
            ans = max(ans, sum(cnt) - sum(cnt[j] for j in range(N) if (i >> j) & 1))
    print(ans)

if __name__ == '__main__':
    main()