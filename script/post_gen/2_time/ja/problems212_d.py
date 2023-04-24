Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    ball = []
    add = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ball.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            ball.sort()
            print(ball[0] + add)
            ball.pop(0)

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    P = []
    X = []
    for i in range(Q):
        p, x = map(int, input().split())
        P.append(p)
        X.append(x)
    print(P)
    print(X)

=======
Suggestion 3

def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    heap = []
    add = 0
    for q in query:
        if q[0] == 1:
            heapq.heappush(heap, q[1] - add)
        elif q[0] == 2:
            add += q[1]
        else:
            print(heapq.heappop(heap) + add)

=======
Suggestion 4

def main():
    import sys
    import heapq
    input = sys.stdin.readline
    Q = int(input())
    q = []
    for _ in range(Q):
        p, *x = map(int, input().split())
        if p == 1:
            heapq.heappush(q, x[0])
        elif p == 2:
            for i in range(len(q)):
                q[i] += x[0]
        else:
            print(heapq.heappop(q))

=======
Suggestion 5

def main():
    import sys
    from heapq import heappush,heappop
    input = sys.stdin.readline
    Q = int(input())
    heap = []
    add = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            heappush(heap,query[1]-add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(heappop(heap)+add)
    return

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    input = sys.stdin.readline

    Q = int(input())
    query = [input().split() for _ in range(Q)]
    q = deque()
    h = []
    for p, x in query:
        if p == "1":
            q.append(int(x))
        elif p == "2":
            q.append(int(x))
        else:
            while h:
                heappop(h)
            while q:
                heappush(h, q.popleft())
            print(h[0])
    return

=======
Suggestion 7

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #初期化
    #ボールに書かれている数を記録する配列
    ball = []
    #袋に入っているボールのうち書かれている数が最小のものの値を記録する変数
    minimum = 0
    #袋に入っているボールのうち書かれている数が最小のものの個数を記録する変数
    min_cnt = 0
    #袋に入っているボールのうち書かれている数が最小のものの個数を記録する変数
    add = 0
    for i in range(Q):
        #操作の種類
        op = query[i][0]
        if op == 1:
            #1 : まだ何も書かれていないボール 1 つに整数 X_i を書き込み、袋に入れる。
            #袋に入っているボールのうち書かれている数が最小のものの個数を記録する変数
            min_cnt = 0
            #袋に入っているボールのうち書かれている数が最小のものの値を記録する変数
            minimum = 0
            #袋に入っているボールのうち書かれている数が最小のものの個数を記録する変数
            add = 0
            #ボールに書かれている数を記録する配列にボールを追加
            ball.append(query[i][1])
        elif op == 2:
            #2 : 袋に入っているすべてのボールについて、そこに書かれてい

=======
Suggestion 8

def main():
    import heapq
    import sys
    input = sys.stdin.readline
    q = int(input())
    # ヒープキューを用いて、最小値を常に取り出せるようにする
    q1 = []
    # 今までの操作の合計値を保持する
    s = 0
    for _ in range(q):
        p, *x = map(int, input().split())
        if p == 1:
            heapq.heappush(q1, x[0] - s)
        elif p == 2:
            s += x[0]
        else:
            print(heapq.heappop(q1) + s)

=======
Suggestion 9

def main():

=======
Suggestion 10

def main():
    Q = int(input())
    # 1回目の操作は、ボールを袋に入れる操作なので、
    # ボールに書かれている数は、その操作の直前の時点での数に等しくなる。
    # そのため、袋に入っているボールのうち書かれている数が最小のものを取り出す操作は、
    # 1回目の操作の直前の時点で、袋に入っているボールのうち書かれている数が最小のものを取り出す操作と等しい。
    # 1回目の操作の直前の時点で、袋に入っているボールのうち書かれている数が最小のものを取り出す操作は、
    # ボールに書かれている数が 0 であるボールを取り出す操作と等しい。
    # したがって、1回目の操作の直前の時点で、袋に入っているボールのうち書かれている数が最小のものを取り出す操作は、
    # ボールに書かれている数が 0 であるボールを取り出す操作と等しい。
    # 1回目の操作の直前の時点で、袋に入っているボールのうち書かれている数が最小のものを取り出す操作は、
    # ボールに書かれている数が 0 であるボールを取り出す操作と等しい。
    # 1回目の操作の直前の時点で、袋に入っているボールのうち書かれている数が最小のものを取り出す操作は、
    # ボールに書かれている数が 0
