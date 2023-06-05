Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    q.reverse()
    bag = []
    for i in range(len(q)):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            print(bag.pop(bag.index(min(bag))))

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    print(a)

=======
Suggestion 3

def main():
    q = int(input())
    balls = []
    for i in range(q):
        p, x = map(int, input().split())
        if p == 1:
            balls.append(x)
        elif p == 2:
            balls = [b + x for b in balls]
        elif p == 3:
            balls.sort()
            print(balls[0])
            balls.pop(0)

=======
Suggestion 4

def main():
    q=int(input())
    p=[]
    x=[]
    for i in range(q):
        p.append(input().split())
    for i in range(q):
        if p[i][0]=='1':
            x.append(int(p[i][1]))
        elif p[i][0]=='2':
            for j in range(len(x)):
                x[j]+=int(p[i][1])
        else:
            print(min(x))
            x.remove(min(x))
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a = a[::-1]
    bag = []
    for i in range(n):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            bag = [x+a[i][1] for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 6

def main():
    # 读入数据
    q = int(input())
    bag = []
    for i in range(q):
        line = input().split()
        if line[0] == '1':
            bag.append(int(line[1]))
        elif line[0] == '2':
            bag = [x + int(line[1]) for x in bag]
        elif line[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 7

def get_input():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return Q, query

=======
Suggestion 8

def main():
    print("hello world")
    return

=======
Suggestion 9

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
        elif query[i][0] == '3':
            print(min(bag))
            bag.remove(min(bag))

main()

=======
Suggestion 10

def main():
    q = int(input())
    query = [list(map(int,input().split())) for _ in range(q)]
    bag = []
    min = 0
    for i in range(q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        else:
            min = min(bag)
            bag.remove(min)
            print(min)
