Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls += [query[1]] * query[2]
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]
    return

=======
Suggestion 2

def main():
    from collections import deque
    q = int(input())
    que = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[1])
        elif query[0] == 2:
            sum = 0
            for j in range(query[1]):
                sum += que.popleft()
            print(sum)

=======
Suggestion 3

def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            balls.append(int(query[1]))
            sum = sum + int(query[1])
        else:
            for i in range(int(query[1])):
                sum = sum - balls[0]
                balls.pop(0)
            print(sum)

=======
Suggestion 4

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.extend([query[1] for i in range(query[2])])
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]

=======
Suggestion 5

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    q = int(input())
    que = deque()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.appendleft([query[1], query[2]])
        else:
            cnt = query[1]
            ans = 0
            while cnt > 0:
                if que[0][1] > cnt:
                    que[0][1] -= cnt
                    ans += que[0][0] * cnt
                    cnt = 0
                else:
                    ans += que[0][0] * que[0][1]
                    cnt -= que[0][1]
                    que.popleft()
            print(ans)

=======
Suggestion 6

def main():
    q = int(input())
    x = []
    c = []
    for i in range(q):
        temp = list(map(int, input().split()))
        if temp[0] == 1:
            x.append(temp[1])
            c.append(temp[2])
        elif temp[0] == 2:
            ball = 0
            for j in range(temp[1]):
                ball += x.pop()
            print(ball)

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    q = int(input())
    d = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.extend([query[1]]*query[2])
        elif query[0] == 2:
            print(sum(list(d)[:query[1]]))

=======
Suggestion 8

def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))

    ans = []
    for i in range(q):
        if a[i][0] == 1:
            ans.append([a[i][1]] * a[i][2])
        else:
            print(sum(ans.pop(0)))

=======
Suggestion 9

def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    balls = []
    for q in query:
        if q[0]==1:
            balls += [q[1]]*q[2]
        else:
            print(sum(balls[:q[1]]))
            balls = balls[q[1]:]

main()

=======
Suggestion 10

def main():
    Q = int(input())
    #print('Q',Q)
    query_list = []
    for i in range(Q):
        query_list.append(input().split())
    #print('query_list',query_list)
    ball_list = []
    for i in range(Q):
        if query_list[i][0] == '1':
            for j in range(int(query_list[i][2])):
                ball_list.append(query_list[i][1])
        else:
            print(sum([int(ball_list.pop(0)) for i in range(int(query_list[i][1]))]))
    #print('ball_list',ball_list)
