Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    l = []
    r = []
    for i in range(n):
        if q[i][0] == 1:
            for j in range(q[i][2]):
                r.append(q[i][1])
        else:
            for j in range(q[i][1]):
                l.append(r[0])
                r.pop(0)
            print(sum(l))

=======
Suggestion 2

def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    balls = []
    for i in range(Q):
        if queries[i][0] == 1:
            for _ in range(queries[i][2]):
                balls.append(queries[i][1])
        elif queries[i][0] == 2:
            print(sum(balls[:queries[i][1]]))

=======
Suggestion 3

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    ans = []
    ball = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                ball.append(query[i][1])
        else:
            ans.append(sum(ball[:query[i][1]]))
            ball = ball[query[i][1]:]
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    q = int(input())
    que = deque()
    for _ in range(q):
        query = list(map(int, input().split()))
        que.append(query)
    que.reverse()
    l = []
    r = []
    for _ in range(q):
        query = que.pop()
        if query[0] == 1:
            l.append(query[1])
            r.append(query[2])
        else:
            ans = 0
            for i in range(len(l)):
                if r[-1] == 0:
                    break
                if l[-1] <= r[-1]:
                    ans += l[-1] * r[-1]
                    r[-1] -= l[-1]
                    l.pop()
                else:
                    ans += r[-1] * r[-1]
                    l[-1] -= r[-1]
                    r.pop()
            print(ans)

=======
Suggestion 5

def main():
    Q = int(input())
    queue = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            queue.append(int(query[1]))
            queue = queue + [int(query[1])] * int(query[2])
        else:
            print(sum(queue[:int(query[1])]))
            queue = queue[int(query[1]):]

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    from bisect import bisect_left

    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    # print(query)

    box = deque()
    sum_ball = 0
    for i in range(q):
        if query[i][0] == 1:
            box.append(query[i][1])
            sum_ball += query[i][1]
        elif query[i][0] == 2:
            if len(box) >= query[i][1]:
                sum_ball -= sum(box[:query[i][1]])
                for j in range(query[i][1]):
                    box.popleft()
            else:
                print(sum_ball)
                continue
        # print(box, sum_ball)
        print(sum_ball)

=======
Suggestion 7

def main():
    from sys import stdin
    input = stdin.readline
    from collections import deque
    Q = int(input())
    d = deque()
    ans = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                d.append(query[1])
        else:
            for j in range(query[1]):
                ans += d.popleft()
            print(ans)
            ans = 0

=======
Suggestion 8

def main():
    from sys import stdin
    from collections import deque
    input = stdin.readline

    Q = int(input())
    queue = deque()
    ans = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            queue.append(query[1])
            ans += query[1]*query[2]
        else:
            ans -= queue.popleft()*query[1]
            print(ans)

main()

=======
Suggestion 9

def main():
    Q = int(input())
    querys = [list(map(int, input().split())) for _ in range(Q)]
    # print(querys)
    balls = []
    for query in querys:
        if query[0] == 1:
            balls.extend([query[1]] * query[2])
        elif query[0] == 2:
            print(sum(balls[:query[1]]))

=======
Suggestion 10

def main():
    # ライブラリのインポート
    import sys

    # 入力の読み込み
    N = int(sys.stdin.readline().rstrip())
    queries = []
    for i in range(N):
        queries.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # ボールの数を管理する配列
    balls = [0] * (10 ** 9 + 1)

    # ボールの合計値を管理する変数
    balls_sum = 0

    # クエリを処理する
    for query in queries:
        if query[0] == 1:
            balls[query[1]] += query[2]
            balls_sum += query[1] * query[2]
        else:
            # ボールの合計値を出力する
            print(balls_sum)
            # ボールの合計値を更新する
            balls_sum -= sum(balls[:query[1]])
            # ボールの数を更新する
            balls = balls[query[1]:]
