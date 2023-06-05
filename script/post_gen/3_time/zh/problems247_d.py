Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    balls = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            balls.append((int(query[1]),int(query[2])))
        if query[0] == '2':
            c = int(query[1])
            if len(balls) == c:
                print(sum([i[0] for i in balls]))
                balls = []
            else:
                print(sum([i[0] for i in balls[:c]]))
                balls = balls[c:]

=======
Suggestion 2

def main():
    q = int(input())
    arr = []
    for i in range(q):
        arr.append(list(map(int, input().split())))
    for item in arr:
        if item[0] == 1:
            print(item[1] * item[2])
        else:
            print(item[1])

=======
Suggestion 3

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(i) for i in input().split()])
    ball = []
    for q in query:
        if q[0] == 1:
            ball = ball + [q[1]] * q[2]
        else:
            print(sum(ball[:q[1]]))
            ball = ball[q[1]:]

=======
Suggestion 4

def main():
    # Q = int(input())
    # for i in range(Q):
    #     query = input().split()
    #     if query[0] == '1':
    #         x = int(query[1])
    #         c = int(query[2])
    #     else:
    #         c = int(query[1])
    #     print(c)
    #     print(x)
    #     print(query)
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            c = int(query[2])
        else:
            c = int(query[1])
        print(c)
        print(x)
        print(query)

=======
Suggestion 5

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    #print(query)
    balls = []
    for i in range(q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                balls.append(query[i][1])
        elif query[i][0] == 2:
            print(sum(balls[:query[i][1]]))

=======
Suggestion 6

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(m) for m in input().split()])
    #print(query)
    cylinder = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                cylinder.append(query[i][1])
        if query[i][0] == 2:
            print(sum(cylinder[:query[i][1]]))
            cylinder = cylinder[query[i][1]:]

=======
Suggestion 7

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            x, c = query.split()[1:]
            balls.extend([int(x)] * int(c))
        else:
            c = int(query.split()[1])
            print(sum(balls[:c]))
            balls = balls[c:]

=======
Suggestion 8

def main():
    q = int(input())
    ans = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            ans += int(query[1]) * int(query[2])
        else:
            print(ans)
            ans = 0

=======
Suggestion 9

def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls += [[int(query[1]), int(query[2])]]
        else:
            sum = 0
            for i in range(int(query[1])):
                sum += balls[i][0]
            print(sum)
            balls = balls[int(query[1]):]
