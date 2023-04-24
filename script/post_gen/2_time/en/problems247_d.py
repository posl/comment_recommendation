Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[2]))
        else:
            print(sum(balls[:int(query[1])]))
            balls = balls[int(query[1]):]

=======
Suggestion 2

def main():
    from collections import deque
    q = int(input())
    d = deque()
    sum = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.append(query[1])
            sum += query[2]
        else:
            for j in range(query[1]):
                sum -= d.popleft()
            print(sum)

=======
Suggestion 3

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
        else:
            print(sum(balls[:int(query[1])]))
            balls = balls[int(query[1]):]

=======
Suggestion 4

def main():
    from collections import deque
    q = int(input())
    d = deque()
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            d.append((int(query[1]), int(query[2])))
        else:
            c = int(query[1])
            s = 0
            while c > 0:
                x, y = d.popleft()
                if c >= y:
                    s += x * y
                    c -= y
                else:
                    s += x * c
                    d.appendleft((x, y-c))
                    c = 0
            print(s)

=======
Suggestion 5

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))

    balls = []
    sum = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1])
            sum += query[i][1] * query[i][2]
        else:
            for j in range(query[i][1]):
                sum -= balls.pop(0)
            print(sum)

=======
Suggestion 6

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))

    balls = []
    sum = 0
    for i in range(Q):
        if queries[i][0] == 1:
            for j in range(queries[i][2]):
                balls.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(queries[i][1]):
                sum += balls[j]
            print(sum)
            sum = 0
            del balls[:queries[i][1]]

=======
Suggestion 7

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append([int(x) for x in input().split()])
    q1 = [x for x in q if x[0] == 1]
    q2 = [x for x in q if x[0] == 2]
    q2 = [x[1] for x in q2]
    q2.reverse()
    for i in range(len(q2)):
        q2[i] = [i, q2[i]]
    q2.reverse()
    q1.reverse()
    ans = []
    for i in range(len(q2)):
        while q2[i][1] > 0:
            if q1[-1][2] <= q2[i][1]:
                ans.append([q1[-1][1], q1[-1][2]])
                q2[i][1] -= q1[-1][2]
                q1.pop()
            else:
                ans.append([q1[-1][1], q2[i][1]])
                q1[-1][2] -= q2[i][1]
                q2[i][1] = 0
    ans.reverse()
    for i in ans:
        print(i[0] * i[1])

=======
Suggestion 8

def main():
    q = int(input())
    balls = {}
    ball_num = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls[ball_num] = [query[1], query[2]]
            ball_num += 1
        else:
            count = query[1]
            sum = 0
            for i in range(ball_num):
                sum += balls[i][0]
                count -= 1
                if count == 0:
                    break
            print(sum)
            ball_num -= query[1]

=======
Suggestion 9

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(query)
    stack = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                stack.append(query[i][1])
        elif query[i][0] == 2:
            sum = 0
            for j in range(query[i][1]):
                sum += stack.pop(0)
            print(sum)

=======
Suggestion 10

def main():
    #print("start")
    #print("end")
