def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    #各文字列に含まれる文字を集合として保持
    S = [set(s) for s in S]
    #全ての文字列を結合した集合
    allS = set()
    for s in S:
        allS |= s
    #全ての文字列を結合した集合の要素数
    allSlen = len(allS)
    #全ての文字列を結合した集合の各要素の出現回数
    allScount = [0]*allSlen
    #各文字列を結合した集合の各要素の出現回数をカウント
    for s in S:
        for i, v in enumerate(allS):
            if v in s:
                allScount[i] += 1
    #出現回数がKと同じ要素数をカウント
    count = 0
    for c in allScount:
        if c == K:
            count += 1
    print(count)

if __name__ == '__main__':
    main()