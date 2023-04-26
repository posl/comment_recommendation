Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    bag = []
    add = 0

    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bag.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(min(bag) + add)
            bag.remove(min(bag))

=======
Suggestion 2

def main():
    import heapq
    Q = int(input())
    que = []
    heapq.heapify(que)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(que, query[1])
        elif query[0] == 2:
            que = [x + query[1] for x in que]
        else:
            print(heapq.heappop(que))

=======
Suggestion 3

def main():
    import heapq
    q = int(input())
    a = []
    heapq.heapify(a)
    total = 0
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            heapq.heappush(a,query[1]-total)
        elif query[0] == 2:
            total += query[1]
        else:
            print(heapq.heappop(a)+total)

=======
Suggestion 4

def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    heap = []
    add = 0
    for p, x in query:
        if p == '1':
            heapq.heappush(heap, int(x) - add)
        elif p == '2':
            add += int(x)
        else:
            print(heapq.heappop(heap) + add)

=======
Suggestion 5

def main():
    import sys
    from heapq import heappush, heappop
    readline = sys.stdin.readline
    Q = int(readline())
    balls = []
    balls_sum = 0
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 1:
            heappush(balls, query[1])
        elif query[0] == 2:
            balls_sum += query[1]
        else:
            print(heappop(balls) + balls_sum)
            balls_sum = 0

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappop, heappush
    # 1行目
    Q = int(input())
    # 2行目以降
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    #print("Q", Q)
    #print("quer

=======
Suggestion 7

def main():
    Q = int(input())
    # 0: 何もしない
    # 1: 1を足す
    # 2: 2を足す
    # 3: 3を足す
    # 4: 4を足す
    # 5: 5を足す
    add = 0
    # 0: 何もしない
    # 1: 1を引く
    # 2: 2を引く
    # 3: 3を引く
    # 4: 4を引く
    # 5: 5を引く
    sub = 0
    # 0: 何もしない
    # 1: 1を掛ける
    # 2: 2を掛ける
    # 3: 3を掛ける
    # 4: 4を掛ける
    # 5: 5を掛ける
    mul = 0
    # 0: 何もしない
    # 1: 1で割る
    # 2: 2で割る
    # 3: 3で割る
    # 4: 4で割る
    # 5: 5で割る
    div = 0
    # 0: 何もしない
    # 1: 1で割った余りを出す
    # 2: 2で割った余りを出す
    # 3: 3で割った余りを出す
    # 4: 4で割った余りを出す
    # 5: 5で割った余りを出す
    rem = 0
    # 0: 何もしない
    # 1: 1で割った余りを出す
    # 2: 2で割った余りを出す
    # 3: 3で割った余りを出す
    # 4:

=======
Suggestion 8

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 1. クエリを処理していく
    # 2. 1の処理で、ボールの数が0になった場合は、ボールを作成して、袋に入れる
    # 3. 2の処理で、袋に入っているボールのうち書かれている数が最小のもの（複数ある場合はそのうちの 1 つ）を取り出し、そこに書かれている数を記録する。その後、そのボールを捨てる。
    # 4. 3の処理で、記録された数を順に出力してください。

    # 1. クエリを処理していく
    # 2. 1の処理で、ボールの数が0になった場合は、ボールを作成して、袋に入れる
    # 3. 2の処理で、袋に入っているボールのうち書かれている数が最小のもの（複数ある場合はそのうちの 1 つ）を取り出し、そこに書かれている数を記録する。その後、そのボールを捨てる。
    # 4. 3の処理で、記録された数を順に出力してください。
    # 5. 4の処理で、記録された数を順に出力してください。
    # 6. 5の処理で、記録された数を順に出力してください。
    # 7. 6の処理で、記録された数を順に出力してください。
    # 8. 7の処理で、記録された数を順に出

=======
Suggestion 9

def main():
    N = int(input())
    que = []
    for i in range(N):
        que.append(input())
    que = que[::-1]
    #print(que)
    ball = []
    add = 0
    while(que):
        q = que.pop()
        q = q.split()
        #print(q)
        if q[0] == "1":
            ball.append(int(q[1]) - add)
        elif q[0] == "2":
            add += int(q[1])
        else:
            min_ball = min(ball)
            print(min_ball + add)
            ball.remove(min_ball)
