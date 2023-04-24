Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                ball.append(int(query[1]))
        else:
            for i in range(int(query[1])):
                ball.pop(0)
            print(sum(ball))
            ball = []

=======
Suggestion 2

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    d = deque()
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                d.append(query[1])
        elif query[0] == 2:
            print(sum([d.popleft() for j in range(query[1])]))

=======
Suggestion 3

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    que = deque()
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            for j in range(q[2]):
                que.append(q[1])
        elif q[0] == 2:
            ans = 0
            for j in range(q[1]):
                ans += que.popleft()
            print(ans)

=======
Suggestion 4

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    Q = int(input())
    que = deque()
    ans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[1])
            que.append(query[2])
        else:
            ans.append(sum(que.popleft() for _ in range(query[1])))
    print(*ans, sep='

')

=======
Suggestion 5

def main():
    N = int(input())
    array = []
    for i in range(N):
        array.append(list(map(int, input().split())))
    ball = []
    for i in range(N):
        if array[i][0] == 1:
            for j in range(array[i][2]):
                ball.append(array[i][1])
        else:
            print(sum(ball[:array[i][1]]))
            del ball[:array[i][1]]
main()

=======
Suggestion 6

def main():
    import sys
    N = int(input())
    A = []
    B = []
    for i in range(N):
        q = sys.stdin.readline().split()
        if q[0] == '1':
            A.append(int(q[1]))
            B.append(int(q[2]))
        else:
            print(sum(A[:int(q[1])]) * sum(B[:int(q[1])]))
            A = A[int(q[1]):]
            B = B[int(q[1]):]

=======
Suggestion 7

def main():
    # 入力
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 処理
    sum = 0
    left = []
    right = []
    for i in range(Q):
        if query[i][0] == 1:
            right.append(query[i][1])
            sum += query[i][1] * query[i][2]
        else:
            for j in range(query[i][1]):
                if len(left) == 0:
                    left.append(right.pop(0))
                else:
                    left.pop(0)
            sum -= sum(left)

    # 出力
    print(sum)

=======
Suggestion 8

def main():
    from collections import deque

    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    ball = deque()
    sum = 0
    for q in range(Q):
        if query[q][0] == 1:
            for _ in range(query[q][2]):
                ball.append(query[q][1])
                sum += query[q][1]
        else:
            for _ in range(query[q][1]):
                sum -= ball.popleft()
            print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    q = []
    for _ in range(N):
        q.append(list(map(int, input().split())))

    l = []
    r = []
    lsum = 0
    rsum = 0
    for i in range(N):
        if q[i][0] == 1:
            r.append(q[i][1])
            rsum += q[i][1] * q[i][2]
        else:
            if q[i][1] > len(l):
                q[i][1] -= len(l)
                l = []
                lsum = 0
                if q[i][1] > len(r):
                    r = []
                    rsum = 0
                else:
                    r = r[q[i][1]:]
                    rsum = sum(r)
            else:
                l = l[q[i][1]:]
                lsum = sum(l)
        if q[i][0] == 2:
            print(lsum + rsum)

=======
Suggestion 10

def main():
    N = int(input())
    for i in range(N):
        # 2 つの整数の入力
        a, b = map(int, input().split())
        # 文字列の入力
        s = input()
        # 出力
        print("{} {}".format(a+b, s))
