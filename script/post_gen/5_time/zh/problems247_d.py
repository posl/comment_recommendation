Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    querys = []
    for i in range(Q):
        querys.append(input())
    balls = []
    for query in querys:
        if query[0] == '1':
            balls.append(query[2:])
        else:
            n = int(query[2:])
            for i in range(n):
                balls.pop(0)
            print(sum([int(ball) for ball in balls]))

=======
Suggestion 2

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    #print(query)
    c = 0
    for i in range(q):
        if query[i][0] == '1':
            c += int(query[i][2])
        else:
            print(c)
            c = 0
main()

=======
Suggestion 3

def main():
    q = int(input())
    #print(q)
    #print(type(q))
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    #print(query)
    #print(type(query))
    #print(query[0])
    #print(type(query[0]))
    #print(query[0][0])
    #print(type(query[0][0]))
    #print(query[0][1])
    #print(type(query[0][1]))
    #print(query[0][2])
    #print(type(query[0][2]))
    #print(query[1])
    #print(type(query[1]))
    #print(query[1][0])
    #print(type(query[1][0]))
    #print(query[1][1])
    #print(type(query[1][1]))
    #print(query[1][2])
    #print(type(query[1][2]))
    #print(query[2])
    #print(type(query[2]))
    #print(query[2][0])
    #print(type(query[2][0]))
    #print(query[2][1])
    #print(type(query[2][1]))
    #print(query[2][2])
    #print(type(query[2][2]))
    #print(query[3])
    #print(type(query[3]))
    #print(query[3][0])
    #print(type(query[3][0]))
    #print(query[3][1])
    #print(type(query[3][1]))
    #print(query[3][2])
    #print(type(query[3][2]))
    #print(query[4])
    #print(type(query[4]))
    #print(query[4][0])
    #print(type(query[4][0]))
    #print(query[4][1])
    #print(type(query[4][1]))
    #print(query[4][2])
    #print(type(query[4][2]))
    #print(query[5])
    #print(type(query[5]))
    #print(query[5][0])
    #print(type(query[5][0]))
    #print(query[5][1])
    #print(type(query[5][1]))
    #print(query[5][2])
    #print(type(query[5][2]))
    #print(query[6])
    #print(type(query[6]))
    #

=======
Suggestion 4

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    ans = 0
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            q.append((int(query[1]), int(query[2])))
            ans += int(query[2])
        else:
            x = int(query[1])
            while x > 0:
                if x >= q[0][1]:
                    x -= q[0][1]
                    ans -= q[0][1] * q[0][0]
                    q.popleft()
                else:
                    ans -= x * q[0][0]
                    q[0] = (q[0][0], q[0][1] - x)
                    x = 0
            print(ans)

=======
Suggestion 5

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(query)

    ball = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                ball.append(query[i][1])
        else:
            print(sum(ball[:query[i][1]]))
            ball = ball[query[i][1]:]

=======
Suggestion 6

def main():
    q = int(input())
    #球的总数
    n = 0
    #圆柱体中球的集合，从左到右
    balls = []
    #圆柱体中球的集合，从右到左
    balls_reverse = []
    #球的总数
    for i in range(q):
        query = input().split()
        #如果是插入
        if query[0] == '1':
            #在圆柱体的右端插入c个球，每个球上写有数字x。
            x = int(query[1])
            c = int(query[2])
            #在圆柱体的右端插入c个球，每个球上写有数字x。
            for i in range(c):
                balls.append(x)
                balls_reverse.insert(0,x)
            n += c
        #如果是取出
        elif query[0] == '2':
            #取出圆柱体中最左边的c个球，并打印出被取出的球上所写的数字之和。
            c = int(query[1])
            sum = 0
            #取出圆柱体中最左边的c个球
            for i in range(c):
                sum += balls[0]
                balls.pop(0)
                balls_reverse.pop()
            #打印出被取出的球上所写的数字之和。
            print(sum)

=======
Suggestion 7

def main():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    balls = []
    for query in queries:
        if query[0] == '1':
            balls.extend([query[1]] * int(query[2]))
        else:
            print(sum(map(int, balls[:int(query[1])])))
            balls = balls[int(query[1]):]

=======
Suggestion 8

def main():
    q = int(input())
    queue = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            queue.append(query[1])
        elif query[0] == "2":
            sum = 0
            for j in range(int(query[1])):
                sum += int(queue.pop(0))
            print(sum)

main()

=======
Suggestion 9

def main():
    Q = int(input())
    query_list = []
    for i in range(Q):
        query_list.append(input().split())

    ball_list = []
    for query in query_list:
        if query[0] == '1':
            for i in range(int(query[2])):
                ball_list.append(query[1])
        else:
            print(sum([int(ball) for ball in ball_list[:int(query[1])]]))
            ball_list = ball_list[int(query[1]):]

=======
Suggestion 10

def main():
    q = int(input())
    for i in range(q):
        a = input().split()
        if a[0] == "1":
            print(a[1], a[2])
