Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #AとBの合計時間を計算
    AB = [a + b for a, b in zip(A, B)]

    #Aの合計時間を計算
    A_sum = sum(A)

    #Bの合計時間を計算
    B_sum = sum(B)

    #Aの合計時間がXを超えている場合
    if A_sum >= X:
        #Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= A[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= A[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 10 ** 18
    for i in range(n):
        ans = min(ans, a[i] * x + b[i] * (n - 1 - i))
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    time = 0
    for i in range(N):
        time += AB[i][0] * AB[i][1]

    time += AB[0][0] * AB[0][1]
    time += AB[0][0] * AB[0][1]

    for i in range(1, N):
        time += AB[i][0] * AB[i][1]

    print(time)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print(ans)
            exit()
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    stage = []
    for i in range(N):
        A, B = map(int, input().split())
        stage.append(A + B)
    stage.sort()
    count = 0
    for i in range(N):
        if X >= stage[i]:
            X -= stage[i]
            count += 1
    if X > 0:
        count -= 1
    print(count)

=======
Suggestion 6

def solve():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][1] for i in range(N)])
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**18
    for i in range(N):
        a, b = AB[i]
        ans = min(ans, a*X+b*(N-i-1))
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    # print(AB)
    AB.reverse()
    # print(AB)
    # print(X)
    count = 0
    time = 0
    for i in range(N):
        if time + AB[i][1] <= X:
            count += 1
            time += AB[i][1]
        else:
            time += AB[i][1]
    # print(count)
    for i in range(N):
        time += AB[i][0]
        count += 1
        if time > X:
            count -= 1
            break
    print(count)

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    #print(ab)
    #print(n,x)
    #n,x = 3,4
    #ab = [[3,4],[2,3],[4,2]]
    #n,x = 10,1000000000
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #ab = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]

    #ab.sort(key=lambda x:x[0])
    #print(ab

=======
Suggestion 10

def calcTime(stages,stageNum):
    time = 0
    for stage in stages:
        time += stage[0] + stage[1] * (stageNum - 1)
    return time
