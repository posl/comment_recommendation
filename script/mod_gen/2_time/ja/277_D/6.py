def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # テーブルに置くカードの候補
    cand = set()
    for a in A:
        cand.add(a)
        cand.add((a + 1) % M)
    # 最小値を求める
    ans = 10 ** 9
    for c in cand:
        # テーブルに置くカードを決める
        table = [0] * M
        table[c] = 1
        # 残ったカードの個数
        rem = N
        # テーブルに置いたカードを手札に戻す
        for i in range(M):
            if table[i] == 1:
                rem += 1
        # 手札に残ったカードの個数
        ans = min(ans, rem)
    print(ans)

if __name__ == '__main__':
    main()