Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append(query[1])
            sum += query[1] * query[2]
        else:
            sum -= balls[0] * query[1]
            balls = balls[query[1]:]
    print(sum)

=======
Suggestion 2

def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
            sum += int(query[2])
        else:
            print(sum)
            sum -= sum(balls[:int(query[1])])
            del balls[:int(query[1])]

=======
Suggestion 3

def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    balls = []
    for query in queries:
        if query[0] == 1:
            balls += [query[1]] * query[2]
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]

=======
Suggestion 4

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[2])
        else:
            print(sum(A[:query[1]]))
            A = A[query[1]:]

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n):
        if l[i][0] == 1:
            l.append([l[i][1],l[i][2]])
        else:
            print(sum([l[j][0] for j in range(len(l)) if j < l[i][1]]))

=======
Suggestion 6

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    balls = []
    for i in range(n):
        if q[i][0] == '1':
            for j in range(int(q[i][2])):
                balls.append(int(q[i][1]))
        else:
            print(sum(balls[:int(q[i][1])]))
            del balls[:int(q[i][1])]
    return 0

=======
Suggestion 7

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    #print(q)
    balls = []
    for i in range(n):
        if q[i][0] == '1':
            for j in range(int(q[i][2])):
                balls.append(int(q[i][1]))
        else:
            print(sum(balls[:int(q[i][1])]))
            del balls[:int(q[i][1])]

=======
Suggestion 8

def main():
    # input
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(list(map(int, input().split())))
    # solve
    cylinder = []
    for query in queries:
        if query[0] == 1:
            cylinder += [query[1]] * query[2]
        elif query[0] == 2:
            print(sum(cylinder[:query[1]]))
            del cylinder[:query[1]]
    # output

=======
Suggestion 9

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    q.reverse()
    ans = []
    balls = []
    for i in range(n):
        if q[i][0] == 1:
            balls.append(q[i][1])
        else:
            ans.append(sum(balls[:q[i][1]]))
            balls = balls[q[i][1]:]
    ans.reverse()
    for i in ans:
        print(i)

=======
Suggestion 10

def problem247_d():
    pass
