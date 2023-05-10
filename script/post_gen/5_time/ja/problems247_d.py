Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    ball = []
    for i in range(Q):
        if query[i][0] == 1:
            ball += [query[i][1]] * query[i][2]
        else:
            print(sum(ball[:query[i][1]]))
            ball = ball[query[i][1]:]

=======
Suggestion 2

def main():
    # 標準入力の取得
    q = int(input())
    # リストを初期化
    L = []
    # クエリの数だけループ
    for i in range(q):
        # クエリを取得
        query = input().split()
        # クエリの種類に応じて処理を分岐
        if query[0] == "1":
            # ボールを入れる
            L.append([int(query[1]), int(query[2])])
        else:
            # ボールを取り出す
            # 取り出すボールの数を取得
            c = int(query[1])
            # 取り出すボールの数だけループ
            total = 0
            for i in range(c):
                # ボールを取り出す
                ball = L.pop(0)
                # 合計値を計算
                total += ball[0] * ball[1]
                # ボールを戻す
                ball[1] -= 1
                if ball[1] > 0:
                    L.insert(0, ball)
            # 合計値を出力
            print(total)

=======
Suggestion 3

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls += [query[1]] * query[2]
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]
    return

=======
Suggestion 4

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for i in range(query[2]):
                balls.append(query[1])
        else:
            sum = 0
            for i in range(query[1]):
                sum += balls[0]
                balls.pop(0)
            print(sum)

=======
Suggestion 5

def main():
    q = int(input())
    ball = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                ball.append(query[1])
        else:
            print(sum(ball[:query[1]]))
            ball = ball[query[1]:]

=======
Suggestion 6

def main():
    from collections import deque
    q = int(input())
    query = deque()
    for i in range(q):
        query.append(list(map(int, input().split())))
    balls = deque()
    for i in range(q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                balls.append(query[i][1])
        else:
            sum = 0
            for j in range(query[i][1]):
                sum += balls.popleft()
            print(sum)

=======
Suggestion 7

def main():
    q = int(input())
    balls = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.extend([query[1]] * query[2])
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]

=======
Suggestion 8

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
        elif query[0] == '2':
            if len(balls) >= int(query[1]):
                print(sum(balls[:int(query[1])]))
                balls = balls[int(query[1]):]
            else:
                print(sum(balls))
                balls = []

=======
Suggestion 9

def main():
    q = int(input())
    ball = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            ball.append(int(query[1]))
        else:
            cnt = int(query[1])
            sum = 0
            for j in range(cnt):
                sum += ball.pop(0)
            print(sum)

=======
Suggestion 10

def main():
    q = int(input())
    #print(q)
    stack = []
    for i in range(q):
        #print(i)
        query = input().split()
        #print(query)
        if query[0] == "1":
            stack.append(int(query[1]))
        else:
            c = int(query[1])
            sum = 0
            for j in range(c):
                sum += stack.pop()
            print(sum)
