def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 2^N通りの組み合わせを調べる
    ans = 0
    for i in range(1 << N):
        # iの各ビットが立っているかどうかで、Sのどの文字列を選択するかを決める
        selected = []
        for j in range(N):
            if i & (1 << j):
                selected.append(S[j])
        # 選択した文字列から、K個の文字列に含まれる文字を集める
        used = set()
        for s in selected:
            for c in s:
                used.add(c)
        # 集めた文字列のうち、K個の文字列に含まれる文字の数を数える
        cnt = 0
        for c in used:
            for s in selected:
                if c in s:
                    cnt += 1
                    break
        # K個の文字列に含まれる文字の数がKと等しいとき、答えとして更新する
        if cnt == K:
            ans = max(ans, len(used))
    print(ans)
main()

if __name__ == '__main__':
    main()