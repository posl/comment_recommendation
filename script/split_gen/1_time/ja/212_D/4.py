def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    #heapq でボールを管理
    #heapq は優先度付きキュー
    #優先度付きキューは、ヒープを用いて実装される
    #ヒープは木構造で、親の要素が子の要素よりも小さい
    #ヒープに要素を追加すると、木構造が崩れることがある
    #そのとき、木構造を再構築する
    #ヒープに要素を取り出すと、木構造が崩れることがある
    #そのとき、木構造を再構築する
    #ヒープは、優先度付きキューの実装に用いられる
    heap = []
    #袋に入っているボールの合計
    total = 0
    for query_i in query:
        if query_i[0] == 1:
            #操作 1 : まだ何も書かれていないボール 1 つに整数 X_i を書き込み、袋に入れる。
            heapq.heappush(heap, query_i[1] - total)
        elif query_i[0] == 2:
            #操作 2 : 袋に入っているすべてのボールについて、そこに書かれている数を、それに X_i を加えたものに書き換える。
            total += query_i[1]
        else:
            #操作 3 : 袋に入っているボールのうち書かれている数が最小のもの（複数ある場合はそのう
