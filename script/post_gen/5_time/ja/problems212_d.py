Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    print('Hello')

=======
Suggestion 2

def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    
    bag = []
    min_value = 0
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            for i in range(len(bag)):
                bag[i] += query[1]
        elif query[0] == 3:
            min_value = min(bag)
            print(min_value)
            bag.remove(min_value)

=======
Suggestion 3

def d():
    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]
    bag = []
    min_num = 10**9
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
            if min_num > query[1]:
                min_num = query[1]
        elif query[0] == 2:
            bag = [i + query[1] for i in bag]
            min_num += query[1]
        else:
            print(min_num)
            bag.remove(min_num)
            if len(bag) != 0:
                min_num = min(bag)
            else:
                min_num = 10**9

=======
Suggestion 4

def main():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    bag = []
    min_value = 0
    for query in queries:
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x + int(query[1]) for x in bag]
        else:
            min_value = min(bag)
            bag.remove(min_value)
            print(min_value)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = deque()
    bag = deque()
    min_num = 0
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            min_num += int(query[i][1])
        else:
            ans.append(min_num+bag.popleft())
            min_num -= ans[-1]
    print('\n'.join(map(str, ans)))

=======
Suggestion 6

def main():
    # 入力
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # 処理
    # ボールの個数
    n = 0
    # ボールの値の合計
    s = 0
    # ボールの最小値
    min_ball = 10 ** 9 + 1
    # ボールの値の合計
    balls = []
    for query in queries:
        if query[0] == 1:
            # ボールを追加
            n += 1
            s += query[1]
            min_ball = min(min_ball, query[1])
            balls.append(query[1])
        elif query[0] == 2:
            # ボールの値を更新
            s += n * query[1]
            min_ball += query[1]
        elif query[0] == 3:
            # ボールを取り出す
            print(balls.pop(0))
            n -= 1
            if n == 0:
                min_ball = 10 ** 9 + 1
            else:
                min_ball = min(balls)

=======
Suggestion 7

def main():
    q = int(input())
    balls = []
    for _ in range(q):
        p = list(map(int, input().split()))
        if p[0] == 1:
            balls.append(p[1])
        elif p[0] == 2:
            balls = [x + p[1] for x in balls]
        elif p[0] == 3:
            print(min(balls))
            balls.remove(min(balls))
    return

main()

=======
Suggestion 8

def main():
    n = int(input())
    q = [list(map(int,input().split())) for _ in range(n)]
    #print(q)
    #print(q[0][1])
    #print(q[0][0])
    #print(q[0][0]==1)
    #print(q[0][0]==2)
    #print(q[0][0]==3)
    #print(q[0][0]==4)
    #print(q[0][0]==5)
    #print(q[0][0]==6)
    #print(q[0][0]==7)
    #print(q[0][0]==8)
    #print(q[0][0]==9)
    #print(q[0][0]==10)
    #print(q[0][0]==11)
    #print(q[0][0]==12)
    #print(q[0][0]==13)
    #print(q[0][0]==14)
    #print(q[0][0]==15)
    #print(q[0][0]==16)
    #print(q[0][0]==17)
    #print(q[0][0]==18)
    #print(q[0][0]==19)
    #print(q[0][0]==20)
    #print(q[0][0]==21)
    #print(q[0][0]==22)
    #print(q[0][0]==23)
    #print(q[0][0]==24)
    #print(q[0][0]==25)
    #print(q[0][0]==26)
    #print(q[0][0]==27)
    #print(q[0][0]==28)
    #print(q[0][0]==29)
    #print(q[0][0]==30)
    #print(q[0][0]==31)
    #print(q[0][0]==32)
    #print(q[0][0]==33)
    #print(q[0][0]==34)
    #print(q[0][0]==35)
    #print(q[0][0]==36)
    #print(q[0][0]==37)
    #print(q[0][0]==38)
    #print(q[0][0]==39)
    #print(q[0][0]==40)
    #print(q[0][0]==41)

=======
Suggestion 9

def main():
    q = int(input())
    x = []
    for _ in range(q):
        x.append(list(map(int, input().split())))
    
    from collections import deque
    bag = deque()
    for i in range(q):
        if x[i][0] == 1:
            bag.append(x[i][1])
        elif x[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += x[i][1]
        else:
            print(bag.popleft())

=======
Suggestion 10

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))

    q3 = []
    for i in range(n):
        if q[i][0] == 3:
            q3.append(i)

    q1 = []
    for i in range(n):
        if q[i][0] == 1:
            q1.append(q[i][1])

    q2 = []
    for i in range(n):
        if q[i][0] == 2:
            q2.append(q[i][1])

    q2sum = sum(q2)
    q2sum2 = 0
    for i in range(n):
        if q[i][0] == 3:
            print(q1[i] + q2sum - q2sum2)
            q2sum2 += q1[i]
