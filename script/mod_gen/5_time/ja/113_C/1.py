def main():
    N, M = map(int, input().split())
    #県ごとの市の出現順を記録する配列
    pre = [[] for i in range(N)]
    #市ごとの年を記録する配列
    year = []
    for i in range(M):
        P, Y = map(int, input().split())
        P -= 1
        year.append(Y)
        pre[P].append((Y, i))
    #県ごとの市の出現順を年の昇順にソートする
    for i in range(N):
        pre[i].sort()
    for i in range(M):
        P = year[i]
        #県ごとの市の出現順を年の昇順にソートしたものから市の番号を探す
        idx = pre[P-1].index((year[i], i))
        #市の番号は1から始まるので+1する
        idx += 1
        #市の番号を6桁の文字列に変換する
        idx = str(idx).zfill(6)
        #県の番号を6桁の文字列に変換する
        P = str(P).zfill(6)
        print(P + idx)

if __name__ == '__main__':
    main()