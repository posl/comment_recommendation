Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    bag = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x + int(query[1]) for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 2

def main():
    n = int(input())
    q = [list(map(int,input().split())) for _ in range(n)]
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 3

def main():
    Q = int(input())
    que = []
    for i in range(Q):
        que.append(list(map(int,input().split())))
    bag = []
    for i in range(Q):
        if que[i][0] == 1:
            bag.append(que[i][1])
        elif que[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += que[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 4

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(input().split())
    
    bag = []
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[i][1])
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 5

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))

    bag = []
    min = 0
    for i in range(q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        elif query[i][0] == 3:
            min = bag.index(min(bag))
            print(bag[min])
            del bag[min]

=======
Suggestion 6

def main():
    q = int(input())
    l = []
    for i in range(q):
        l.append(list(map(int, input().split())))
    l.reverse()
    bag = []
    for i in range(q):
        if l[i][0] == 1:
            bag.append(l[i][1])
        elif l[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += l[i][1]
        else:
            bag.sort()
            print(bag.pop())

=======
Suggestion 7

def main():
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    bag = []
    min_value = 0
    for p, x in query:
        if p == 1:
            bag.append(x - min_value)
        elif p == 2:
            min_value += x
        else:
            print(bag.pop() + min_value)

=======
Suggestion 8

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    #print(query)
    bag = []
    for i in range(Q):
        #print("query[i][0] = ", query[i][0])
        #print("query[i][1] = ", query[i][1])
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 9

def main():
    q = int(input())
    balls = []
    ball_sum = 0
    min_ball = 10**9
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            balls.append(query[1])
            ball_sum += query[1]
            if min_ball > query[1]:
                min_ball = query[1]
        elif query[0] == 2:
            ball_sum += query[1] * len(balls)
            min_ball += query[1]
        elif query[0] == 3:
            print(min_ball)
            ball_sum -= min_ball
            min_ball = 10**9
            if len(balls) > 0:
                min_ball = min(balls)
    return

=======
Suggestion 10

def main():
    n = int(input())
    #print(n)
    ball = []
    for i in range(n):
        #print(i)
        a = input()
        #print(a)
        if a[0] == '1':
            b = a.split()
            #print(b)
            ball.append(int(b[1]))
            #print(ball)
        elif a[0] == '2':
            b = a.split()
            #print(b)
            for j in range(len(ball)):
                ball[j] += int(b[1])
            #print(ball)
        else:
            print(min(ball))
            ball.remove(min(ball))
            #print(ball)
