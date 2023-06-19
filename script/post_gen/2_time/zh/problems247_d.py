Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    ball = []
    for i in range(q):
        if query[i][0] == '1':
            for j in range(int(query[i][2])):
                ball.append(int(query[i][1]))
        elif query[i][0] == '2':
            sum = 0
            for j in range(int(query[i][1])):
                sum += ball.pop(0)
            print(sum)

=======
Suggestion 2

def main():
    Q = int(input())
    queue = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            queue.append([int(query[1]), int(query[2])])
        else:
            c = int(query[1])
            sum = 0
            for j in range(c):
                sum += queue[j][0]
            print(sum)
            queue = queue[c:]

=======
Suggestion 3

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())

    for i in range(q):
        if query[i][0] == "1":
            #print("1")
            #print(query[i][1])
            #print(query[i][2])
            continue
        if query[i][0] == "2":
            #print("2")
            #print(query[i][1])
            continue

=======
Suggestion 4

def main():
    Q = int(input())
    ball = []
    sum = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                ball.append(int(query[1]))
        else:
            for i in range(int(query[1])):
                sum += ball[0]
                del ball[0]
            print(sum)
            sum = 0

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    q = int(input())
    data = []
    for i in range(q):
        data.append(input().split())
    for i in range(q):
        if data[i][0] == '1':
            data[i][1] = int(data[i][1])
            data[i][2] = int(data[i][2])
            if i == 0:
                ball = [data[i][1]]*data[i][2]
            else:
                ball = ball + [data[i][1]]*data[i][2]
        else:
            data[i][1] = int(data[i][1])
            if i == 0:
                print(sum(ball[:data[i][1]]))
                ball = ball[data[i][1]:]
            else:
                print(sum(ball[:data[i][1]]))
                ball = ball[data[i][1]:]

=======
Suggestion 7

def main():
    q = int(input())
    ans = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ans += query[1] * query[2]
        elif query[0] == 2:
            print(ans)
            ans -= query[1]

=======
Suggestion 8

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    cylinder = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                cylinder.append(query[i][1])
        elif query[i][0] == 2:
            print(sum(cylinder[:query[i][1]]))
            cylinder = cylinder[query[i][1]:]

=======
Suggestion 9

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    balls = []
    sum = 0
    for q in query:
        if q[0] == 1:
            balls.extend([q[1]] * q[2])
        else:
            for i in range(q[1]):
                sum += balls.pop(0)
            print(sum)
            sum = 0

=======
Suggestion 10

def solve():
    q = int(input())
    query = [input().split() for _ in range(q)]
    query = [(int(q[0]), int(q[1]), int(q[2])) for q in query]
    query = [(q[0], q[1], q[2]) if q[0] == 1 else (q[0], q[1], 0) for q in query]

    balls = []
    sum = 0

    for q in query:
        if q[0] == 1:
            for i in range(q[2]):
                balls.append(q[1])
                sum += q[1]
        else:
            for i in range(q[1]):
                sum -= balls[i]
            balls = balls[q[1]:]
            print(sum)
