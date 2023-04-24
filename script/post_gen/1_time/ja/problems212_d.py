Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    min_num = 0
    add_num = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            min_num = min(min_num, query[1] - add_num)
        elif query[0] == 2:
            add_num += query[1]
        else:
            print(min_num + add_num)

=======
Suggestion 2

def main():
    q = int(input())
    num = []
    add = 0
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            num.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(min(num) + add)
            num.remove(min(num))

=======
Suggestion 3

def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    B = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(A, query[1])
        elif query[0] == 2:
            B.append(query[1])
        else:
            print(heapq.heappop(A) + sum(B))
            if len(A) == 0:
                A = B
                B = []
            else:
                B = []
    return

=======
Suggestion 4

def main():
    Q = int(input())
    que = []
    for i in range(Q):
        que.append(list

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    import heapq
    q = int(input())
    que = []
    for i in range(q):
        que.append(list(map(int,input().split())))
    #print(que)
    num = 0
    for i in range(q):
        if que[i][0] == 1:
            heapq.heappush(que[i],que[i][1]-num)
        elif que[i][0] == 2:
            num += que[i][1]
        else:
            print(heapq.heappop(que[i])+num)
            que[i] = []

=======
Suggestion 7

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    balls = []
    balls.append(0)
    balls.append(0)
    add = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1] - add)
        elif query[i][0] == 2:
            add += query[i][1]
        else:
            min_value = min(balls)
            print(min_value + add)
            balls.remove(min_value)

=======
Suggestion 8

def main():
    import heapq
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(i) for i in input().split()])
    
    #Q = 5
    #query = [
    #    [1, 3],
    #    [1, 5],
    #    [3],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 6
    #query = [
    #    [1, 1000000000],
    #    [2, 1000000000],
    #    [2, 1000000000],
    #    [2, 1000000000],
    #    [2, 1000000000],
    #    [3],
    #]
    
    #Q = 2
    #query = [
    #    [1, 1],
    #    [3],
    #]
    
    #Q = 3
    #query = [
    #    [1, 1],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 5
    #query = [
    #    [1, 1],
    #    [2, 2],
    #    [1, 1],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 5
    #query = [
    #    [1, 1],
    #    [2, 2],
    #    [1, 1],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 5
    #query = [
    #    [1, 1],
    #    [2, 2],
    #    [1, 1],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 5
    #query = [
    #    [1, 1],
    #    [2, 2],
    #    [1, 1],
    #    [2, 2],
    #    [3],
    #]
    
    #Q = 5
    #query = [
    #    [1, 1],

=======
Suggestion 9

def main():
    Q = int(input())
    q = []
    for _ in range(Q):
        q.append(input())
    #print(q)
    #print(Q)
    #print(q)
    #print(q[0])
    #print(q[0].split())
    #print(q[0].split()[0])
    #print(q[0].split()[1])
    #print(q[1].split()[0])
    #print(q[1].split()[1])
    #print(q[2].split()[0])
    #print(q[2].split()[1])
    #print(q[3].split()[0])
    #print(q[3].split()[1])
    #print(q[4].split()[0])
    #print(q[4].split()[1])
    #print(q[5].split()[0])
    #print(q[5].split()[1])
    #print(q[6].split()[0])
    #print(q[6].split()[1])
    #print(q[7].split()[0])
    #print(q[7].split()[1])
    #print(q[8].split()[0])
    #print(q[8].split()[1])
    #print(q[9].split()[0])
    #print(q[9].split()[1])
    #print(q[10].split()[0])
    #print(q[10].split()[1])
    #print(q[11].split()[0])
    #print(q[11].split()[1])
    #print(q[12].split()[0])
    #print(q[12].split()[1])
    #print(q[13].split()[0])
    #print(q[13].split()[1])
    #print(q[14].split()[0])
    #print(q[14].split()[1])
    #print(q[15].split()[0])
    #print(q[15].split()[1])
    #print(q[16].split()[0])
    #print(q[16].split()[1])
    #print(q[17].split()[0])
    #print(q[17].split()[1])
    #print(q[18].split()[0])
    #print(q[18].split()[1])
    #print(q[19].split()[0])
    #print(q[19].split()[1])
    #print(q[

=======
Suggestion 10

def main():
    q = int(input())
    #操作1のボールの値を入れるリスト
    balls = []
    #操作2の加算値を入れる変数
    add_num = 0
    for i in range(q):
        query = list(map(int, input().split()))
        #操作1
        if query[0] == 1:
            balls.append(query[1] - add_num)
        #操作2
        elif query[0] == 2:
            add_num += query[1]
        #操作3
        elif query[0] == 3:
            min_num = min(balls)
            print(min_num + add_num)
            balls.remove(min_num)
