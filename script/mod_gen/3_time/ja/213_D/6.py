def main():
    N = int(input())
    edge_list = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        edge_list[A-1].append(B-1)
        edge_list[B-1].append(A-1)
    #print(edge_list)
    # 0からスタート
    start = 0
    # 0からスタートしたので、0を訪問済みにする
    visited = [False] * N
    visited[0] = True
    # 0をスタートにして、スタックに積む
    stack = [0]
    # 答え
    ans = [1]
    # スタックが空になるまで（スタックが空になるということは、全ての都市を訪問したということ）
    while stack:
        # スタックから都市を取り出す
        city = stack.pop()
        # 取り出した都市から直接つながっている都市を調べる
        for next_city in edge_list[city]:
            # 次の都市が訪問済みでないなら
            if not visited[next_city]:
                # 次の都市を訪問済みにする
                visited[next_city] = True
                # 次の都市をスタックに積む
                stack.append(next_city)
                # 答えに次の都市を追加する
                ans.append(next_city+1)
                # 次の都市に移動したので、次の都市から直接つながっている都市を調べる
                break
        # 次の都市が訪問済みであるか、もしくは、次の都市が存在しないなら
        else:
            # 現在いる都市がスタート地点でないなら
            if city != start:
                # 現在いる都市をスタックに積む
                stack

if __name__ == '__main__':
    main()