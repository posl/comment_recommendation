Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    bag = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[1])
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        x = input().split()
        if int(x[0]) == 1:
            a.append(int(x[1]))
        elif int(x[0]) == 2:
            a = [i + int(x[1]) for i in a]
        else:
            print(min(a))
            a.remove(min(a))

=======
Suggestion 3

def main():
    n = int(input())
    balls = []
    for i in range(n):
        p = input().split()
        if p[0] == "1":
            balls.append(int(p[1]))
        elif p[0] == "2":
            for j in range(len(balls)):
                balls[j] += int(p[1])
        else:
            print(min(balls))
            balls.remove(min(balls))

=======
Suggestion 4

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))

    bag = []
    for q in queries:
        if q[0] == 1:
            bag.append(q[1])
        elif q[0] == 2:
            for i in range(len(bag)):
                bag[i] += q[1]
        elif q[0] == 3:
            print(min(bag))
            bag.pop(bag.index(min(bag)))

=======
Suggestion 5

def main():
    Q = int(input())
    operations = []
    for i in range(Q):
        operations.append(list(map(int, input().split())))

    balls = []
    for i in range(Q):
        if operations[i][0] == 1:
            balls.append(operations[i][1])
        elif operations[i][0] == 2:
            balls = [x + operations[i][1] for x in balls]
        else:
            print(min(balls))
            balls.remove(min(balls))

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))

    bag = []
    for i in x:
        if i[0] == 1:
            bag.append(i[1])
        elif i[0] == 2:
            for j in range(len(bag)):
                bag[j] += i[1]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.reverse()
    bag = []
    for i in range(n):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += a[i][1]
        elif a[i][0] == 3:
            bag.sort()
            print(bag.pop(0))
    return 0

=======
Suggestion 8

def main():
    #n = input()
    #a = int(input())
    #b, c = map(int, input().split())
    #s = input()
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = input().split()
    #a = [int(input()) for i in range(n)]
    #a = [int(input().split()) for i in range(n)]
    #a = [input().split() for i in range(n)]
    #a = [int(input()) for i in range(n)]
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]

    q = int(input())
    x = []
    for i in range(q):
        x.append(list(map(int, input().split())))

    bag = []
    for i in range(q):
        if x[i][0] == 1:
            bag.append(x[i][1])
        elif x[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += x[i][1]
        elif x[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 9

def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        line = input()
        line = line.split(" ")
        p = int(line[0])
        if p == 1:
            x = int(line[1])
            balls.append(x)
        elif p == 2:
            x = int(line[1])
            for j in range(len(balls)):
                balls[j] += x
        else:
            balls.sort()
            print(balls.pop(0))

=======
Suggestion 10

def main():
    # Read from STDIN
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    # Solve
    bag = []
    bag_min = 10**9 + 1
    bag_min_index = None
    for i in range(Q):
        if queries[i][0] == 1:
            bag.append(queries[i][1])
            if queries[i][1] < bag_min:
                bag_min = queries[i][1]
                bag_min_index = len(bag) - 1
        elif queries[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += queries[i][1]
                if bag[j] < bag_min:
                    bag_min = bag[j]
                    bag_min_index = j
        else:
            print(bag[bag_min_index])
            del bag[bag_min_index]
            bag_min = 10**9 + 1
            for j in range(len(bag)):
                if bag[j] < bag_min:
                    bag_min = bag[j]
                    bag_min_index = j
