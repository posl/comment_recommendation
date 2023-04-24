Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            print("insert", x, c)
        elif query[0] == 2:
            c = query[1]
            print("take", c)
        else:
            print("error")
            return

=======
Suggestion 2

def main():
    Q = int(input())
    cylinder = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            cylinder += [query[1]] * query[2]
        else:
            print(sum(cylinder[:query[1]]))
            cylinder = cylinder[query[1]:]

=======
Suggestion 3

def main():
    Q = int(input())
    cylinder = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            cylinder.extend([int(query[1])] * int(query[2]))
        else:
            print(sum(cylinder[:int(query[1])]))
            del cylinder[:int(query[1])]

=======
Suggestion 4

def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                ball.append(query[1])
        else:
            print(sum(ball[:query[1]]))
            del ball[:query[1]]

=======
Suggestion 5

def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            balls += [int(query[1])] * int(query[2])
        else:
            print(sum(balls[:int(query[1])]))
            balls = balls[int(query[1]):]

=======
Suggestion 6

def main():
    Q = int(input())
    ans = []
    total = 0
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            total += int(query[1]) * int(query[2])
        else:
            ans.append(total)
            total = 0
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.readline
    Q = int(readline())
    cylinder = []
    for _ in range(Q):
        query = readline().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                cylinder.append(int(query[1]))
        else:
            print(sum(cylinder[:int(query[1])]))
            cylinder = cylinder[int(query[1]):]

main()

=======
Suggestion 8

def main():
    q = int(input())
    queue = []
    for i in range(q):
        queue.append(input().split())
    for i in range(q):
        if queue[i][0] == '1':
            for j in range(int(queue[i][2])):
                queue.append([queue[i][1]])
        else:
            sum = 0
            for j in range(int(queue[i][1])):
                sum += int(queue[j][0])
            print(sum)
            for j in range(int(queue[i][1])):
                del queue[0]
main()

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline

    Q = int(input())
    ans = []
    # 総和
    total = 0
    # 操作後のリスト
    li = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            li += [x] * c
            total += x * c
        else:
            c = query[1]
            ans.append(total)
            total -= sum(li[:c])
            li = li[c:]
    print('

'.join(map(str, ans)))

=======
Suggestion 10

def main():
    # Put your code here
    pass
