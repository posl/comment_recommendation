Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append([query[1], query[2]])
        elif query[0] == 2:
            takeout = query[1]
            sum = 0
            for i in range(len(balls)):
                sum += balls[i][0] * balls[i][1]
                if sum >= takeout:
                    balls[i][1] -= (sum - takeout) // balls[i][0]
                    if (sum - takeout) % balls[i][0] != 0:
                        balls[i][1] -= 1
                    break
            while balls[0][1] == 0:
                balls.pop(0)
            print(sum)

=======
Suggestion 2

def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append([query[1], query[2]])
        else:
            sum = 0
            for j in range(query[1]):
                sum += balls[j][0]
            print(sum)
            balls = balls[query[1]:]

=======
Suggestion 3

def main():
    n = int(input())
    balls = []
    for i in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.extend([query[1]] * query[2])
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]

=======
Suggestion 4

def solve():
    from collections import deque
    Q = int(input())
    que = deque()
    s = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[2])
            s += query[1] * query[2]
        else:
            while query[1] > 0:
                if query[1] >= que[0]:
                    query[1] -= que[0]
                    s -= que[0] * que.popleft()
                else:
                    s -= query[1] * que[0]
                    que[0] -= query[1]
                    query[1] = 0
        if query[0] == 2:
            print(s)

=======
Suggestion 5

def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input().split()
        if s[0] == "1":
            if s[1] in d:
                d[s[1]] += int(s[2])
            else:
                d[s[1]] = int(s[2])
        else:
            for i in sorted(d.keys())[:int(s[1])]:
                print(d[i])
                del d[i]

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    d = deque()
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            d.append(int(query[1]))
        else:
            c = int(query[1])
            s = 0
            while c > 0:
                x = d.popleft()
                s += x
                c -= 1
            print(s)

=======
Suggestion 7

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))

    balls = []
    num = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1])
            num += query[i][2]
        else:
            print(sum(balls[:query[i][1]]) + num)
            balls = balls[query[i][1]:]

=======
Suggestion 8

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    q = q[::-1]
    ans = []
    s = 0
    for i in range(n):
        if q[i][0] == "2":
            s += int(q[i][1])
            ans.append(s)
        else:
            s = 0
    ans = ans[::-1]
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    q = int(input())
    # print(q)
    c = []
    x = []
    for i in range(q):
        query = input().split()
        # print(query)
        if query[0] == '1':
            x.append(int(query[1]))
            c.append(int(query[2]))
        else:
            c_ = int(query[1])
            sum_ = 0
            for i in range(len(c)):
                if c_ > 0:
                    if c[i] <= c_:
                        sum_ += c[i] * x[i]
                        c_ -= c[i]
                        c[i] = 0
                    else:
                        sum_ += c_ * x[i]
                        c[i] -= c_
                        c_ = 0
            print(sum_)

=======
Suggestion 10

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    # print(queries)
    # print(Q)

    balls = []
    sum = 0
    for i in range(Q):
        if queries[i][0] == 1:
            for j in range(queries[i][2]):
                balls.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(queries[i][1]):
                sum += balls.pop(0)
            print(sum)
            sum = 0
        # print(balls)
        # print(sum)
