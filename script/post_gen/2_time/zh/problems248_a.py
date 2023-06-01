Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(N):
        print("Hello World")

=======
Suggestion 2

def main():
    q = int(input())
    c = [0] * q
    x = [0] * q
    for i in range(q):
        c[i], x[i] = map(int, input().split())

    # print(c)
    # print(x)

    # 計算
    sum = 0
    for i in range(q):
        if c[i] == 1:
            sum += x[i]
        elif c[i] == 2:
            print(sum)
            sum = 0
        else:
            print("error")
            return

=======
Suggestion 3

def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    n = int(readline())
    a = []
    b = []
    for _ in range(n):
        q = readline().split()
        if q[0] == "1":
            x, c = int(q[1]), int(q[2])
            a.append((x, c))
        else:
            c = int(q[1])
            b.append(c)
    a.reverse()
    for c in b:
        s = 0
        while c > 0:
            if len(a) == 0:
                break
            x, d = a[-1]
            a.pop()
            if c >= d:
                s += x * d
                c -= d
            else:
                s += x * c
                a.append((x, d - c))
                break
        write("%d\n" % s)
    return


main()

=======
Suggestion 4

def solve():
    from collections import deque
    q = int(input())
    que = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.appendleft([query[1], query[2]])
        else:
            ans = 0
            for i in range(query[1]):
                a = que.pop()
                ans += a[0]
                a[1] -= 1
                if a[1] != 0:
                    que.append(a)
            print(ans)


solve()

=======
Suggestion 5

def main():
    q = int(input())
    ans = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ans += query[1] * query[2]
        else:
            print(ans)
            ans = 0

=======
Suggestion 6

def main():
    Q = int(input())
    balls = []
    total = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
            total += int(query[2])
        else:
            print(total)
            total -= balls.pop(0)
    return

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    q = int(input())
    queries = [sys.stdin.readline().strip() for i in range(q)]

    ans = deque()
    num = 0
    for query in queries:
        q = query.split()
        if q[0] == '1':
            num += int(q[2])
            if q[1] == '1':
                ans.appendleft(int(q[2]))
            else:
                ans.append(int(q[2]))
        else:
            temp = 0
            for i in range(int(q[1])):
                temp += ans.popleft()
            print(temp)
            num -= int(q[1])
    return

=======
Suggestion 8

def main():
    q = int(input())
    a = [0] * q
    b = [0] * q
    for i in range(q):
        a[i], b[i] = map(int, input().split())

    s = []
    for i in range(q):
        if a[i] == 1:
            s.append(b[i])
        else:
            ans = 0
            for j in range(b[i]):
                ans += s[j]
            print(ans)
            s = s[b[i]:]

=======
Suggestion 9

def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(input().split())
    for i in range(q):
        if int(a[i][0]) == 1:
            print(a[i][1] + a[i][2])
        else:
            print(int(a[i][1]) + int(a[i][1]) + 1)
main()

=======
Suggestion 10

def main():
    Q = int(input())
    # query = []
    # for i in range(Q):
    #     query.append(list(map(int, input().split())))
    query = [list(map(int, input().split())) for i in range(Q)]
    # print(query)
    ans = []
    for i in range(Q):
        if query[i][0] == 1:
            ans.append(query[i][1] * query[i][2])
        else:
            ans.append(sum(ans[:query[i][1]]))
    # print(ans)
    for i in ans:
        print(i)
