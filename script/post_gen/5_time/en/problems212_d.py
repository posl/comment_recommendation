Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    a = []
    for i in range(q):
        p = list(map(int, input().split()))
        if p[0] == 1:
            a.append(p[1])
        elif p[0] == 2:
            for j in range(len(a)):
                a[j] += p[1]
        else:
            print(min(a))
            a.remove(min(a))

=======
Suggestion 2

def main():
    q = int(input())
    balls = []
    for i in range(q):
        line = input().split()
        if line[0] == "1":
            balls.append(int(line[1]))
        elif line[0] == "2":
            balls = [x + int(line[1]) for x in balls]
        elif line[0] == "3":
            print(min(balls))
            balls.remove(min(balls))

=======
Suggestion 3

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
Suggestion 4

def main():
    # input
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # compute

=======
Suggestion 5

def main():
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    bag = []
    smallest = 0
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            bag = [i+query[1] for i in bag]
        elif query[0] == 3:
            smallest = min(bag)
            bag.remove(smallest)
            print(smallest)

=======
Suggestion 6

def main():
    N = int(input())
    queries = []
    for i in range(N):
        queries.append(input().split())
    #print(queries)
    balls = []
    for i in range(N):
        if queries[i][0] == '1':
            balls.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            for j in range(len(balls)):
                balls[j] += int(queries[i][1])
        elif queries[i][0] == '3':
            print(min(balls))
            balls.remove(min(balls))
    #print(balls)

=======
Suggestion 7

def solve():
    from heapq import heappush, heappop
    from sys import stdin, stdout
    input = stdin.readline
    print = stdout.write
    q = int(input())
    bag = []
    offset = 0
    for _ in range(q):
        p, *x = map(int, input().split())
        if p == 1:
            heappush(bag, x[0] - offset)
        elif p == 2:
            offset += x[0]
        else:
            print(f'{heappop(bag) + offset}\n')
    return 0

=======
Suggestion 8

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append([int(i) for i in input().split()])

    output = []
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            output.append(min(bag))
            bag.remove(min(bag))

    for i in output:
        print(i)

=======
Suggestion 9

def main():
    # input
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    #s = input()
    #s = input().split()
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [int(input()) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [input() for i in range(h)]
    #a = [input().split() for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]

    # solve
    import heapq
    hq = []
    add = 0
    for i in range(n):
        p = input().split()
        if p[0] == '1':
            heapq.heappush(hq, int(p[1]) - add)
        elif p[0] == '2':
            add += int(p[1])
        else:
            print(heapq.heappop(hq) + add)

    # output

=======
Suggestion 10

def solve(N, A):
    return 0
