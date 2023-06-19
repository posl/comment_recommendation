Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        p, x = map(int, input().split())
        if p == 1:
            a[i] = x
        elif p == 2:
            for j in range(n):
                a[j] += x
        else:
            print(min(a))
            a.remove(min(a))
            a.append(0)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            ball.append(int(query[1]))
        elif query[0] == "2":
            for j in range(len(ball)):
                ball[j] += int(query[1])
        elif query[0] == "3":
            print(min(ball))
            ball.remove(min(ball))

=======
Suggestion 4

def main():
    N = int(input())
    bag = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x+int(query[1]) for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappush, heappop
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    bag = []
    add = 0
    for p, x in query:
        if p == 1:
            heappush(bag, x - add)
        elif p == 2:
            add += x
        else:
            print(heappop(bag) + add)

=======
Suggestion 6

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int,input().split())))
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            bag.sort()
            print(bag[0])
            bag.pop(0)

=======
Suggestion 7

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    bag = []
    for i in range(Q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        elif query[i][0] == 3:
            print(min(bag))
            bag.pop(bag.index(min(bag)))

=======
Suggestion 8

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
Suggestion 9

def main():
    Q = int(input())
    query = [input().split() for i in range(Q)]

    bag = []
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            bag = [x + int(query[i][1]) for x in bag]
        elif query[i][0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 10

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    bag = []
    for i in range(q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))
