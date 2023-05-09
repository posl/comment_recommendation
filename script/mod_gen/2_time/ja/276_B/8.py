def main():
    N, M = map(int, input().split())
    # 都市をキーにして、道路で直接結ばれた都市のリストを値とする辞書を作成
    d = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        d[A].append(B)
        d[B].append(A)
    # 道路で直接結ばれた都市のリストの要素数と、その都市の番号を出力
    for i in range(1, N + 1):
        print(len(d[i]), *sorted(d[i]))

if __name__ == '__main__':
    main()