Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        if query[i][0] == 1

=======
Suggestion 2

def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            ans.append(query[i][1])
        else:
            ans.pop(0)
    print(sum(list(map(int,ans))))

=======
Suggestion 3

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    r = []
    for i in query:
        if i[0] == 1:
            r.append(i[1] * i[2])
        else:
            print(sum(r[:i[1]]))
main()

=======
Suggestion 4

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    count = 0
    for i in range(Q):
        if query[i][0] == 1:
            count += query[i][1]*query[i][2]
        else:
            print(count)
            count = 0

=======
Suggestion 5

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    left = 0
    right = 0
    sum = 0
    for i in range(Q):
        if query[i][0] == 1:
            right = right + query[i][2]
            sum = sum + query[i][1] * query[i][2]
        else:
            sum = sum - query[i][1] * query[i][2]
            left = left + query[i][2]
        print(sum)

=======
Suggestion 6

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
        else:
            print(sum(cylinder[:query[i][1]]))
            cylinder = cylinder[query[i][1]:]

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N):
        print(i)

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == 1:
            for j in range(a[2]):
                s.append(a[1])
        else:
            print(sum(s[:a[1]]))
            s = s[a[1]:]

=======
Suggestion 9

def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    balls = []
    sum = 0
    for q in query:
        if q[0] == '1':
            balls.extend([int(q[1])] * int(q[2]))
        else:
            for i in range(int(q[1])):
                sum += balls.pop(0)
            print(sum)
            sum = 0

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().split())
    a = list(map(lambda x: list(map(int, x)), a))
    b = []
    for i in range(n):
        if a[i][0] == 1:
            for j in range(a[i][2]):
                b.append(a[i][1])
        else:
            print(sum(b[:a[i][1]]))
