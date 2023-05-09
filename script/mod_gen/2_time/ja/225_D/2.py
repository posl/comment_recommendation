def main():
    N, Q = map(int, input().split())
    train = [[i, i, i] for i in range(N + 1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            if query[0] == 1:
                # query[1]の後ろにquery[2]をつなげる
                train[query[1]][2] = query[2]
                train[query[2]][0] = query[1]
            else:
                # query[1]の後ろを切り離す
                train[train[query[1]][2]][0] = query[1]
                train[query[1]][2] = query[1]
        else:
            # query[1]が含まれる連結成分に属する電車の番号を出力
            ans = []
            i = query[1]
            while train[i][0] != i:
                ans.append(i)
                i = train[i][0]
            ans.append(i)
            print(len(ans), *ans)

if __name__ == '__main__':
    main()