Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    #print("start")
    #读取数据
    #第一行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    N = int(line[0])
    M = int(line[1])
    #print(N,M)
    #第二行到第M+1行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    A = []
    B = []
    for i in range(M):
        A.append(int(line[2*i]))
        B.append(int(line[2*i+1]))
    #print(A)
    #print(B)
    #第M+2行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    K = int(line[0])
    #print(K)
    #第M+3行到第M+K+2行
    line = input()
    #print(line)
    line = line.split()
    #print(line)
    C = []
    D = []
    for i in range(K):
        C.append(int(line[2*i]))
        D.append(int(line[2*i+1]))
    #print(C)
    #print(D)
    #数据读取完毕
    #print("end")
    #print("start")
    #计算
    #print(N,M,K)
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    #计算满足条件的个数
    count = 0
    for i in range(K):
        #print(i)
        #print(C[i])
        #print(D[i])
        #print(A)
        #print(B)
        #print(C)
        #print(D)
        if C[i] in A and D[i] in B:
            count += 1
    #print(count)
    #计算
    #print("end")
    #输出
    print(count)
    return

=======
Suggestion 3

def judge(plate,condition):
    for i in range(condition[0]-1,condition[1]):
        if plate[i] == 0:
            return False
    return True

N,M = map(int,input().split())
condition = []
for i in range(M):
    condition.append(list(map(int,input().split())))
K = int(input())
ball = []
for i in range(K):
    ball.append(list(map(int,input().split())))

ans = 0
for i in range(2**K):
    plate = [0 for i in range(N)]
    for j in range(K):
        if((i >> j) & 1):
            plate[ball[j][1]-1] += 1
        else:
            plate[ball[j][0]-1] += 1
    cnt = 0
    for j in range(M):
        if judge(plate,condition[j]):
            cnt += 1
    ans = max(ans,cnt)
print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if balls[AB[j][0]-1] >= 1 and balls[AB[j][1]-1] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        balls = [False] * N
        for j in range(K):
            if i >> j & 1:
                balls[CD[j][0] - 1] = True
            else:
                balls[CD[j][1] - 1] = True
        cnt = 0
        for j in range(M):
            if balls[AB[j][0] - 1] and balls[AB[j][1] - 1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        cnt = 0
        for a, b in AB:
            if balls[a] and balls[b]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        cnt = 0
        balls = set()
        for j in range(k):
            if (i >> j) & 1:
                balls.add(cd[j][0])
            else:
                balls.add(cd[j][1])
        for a, b in ab:
            if a in balls and b in balls:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2**k):
        balls = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                balls[cd[j][0]-1] += 1
            else:
                balls[cd[j][1]-1] += 1

        cnt = 0
        for j in range(m):
            if balls[ab[j][0]-1] and balls[ab[j][1]-1]:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        tmp = [0]*n
        for j in range(k):
            if (i >> j) & 1:
                tmp[cd[j][0]-1] += 1
            else:
                tmp[cd[j][1]-1] += 1
        cnt = 0
        for a, b in ab:
            if tmp[a-1] and tmp[b-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2**k):
        ball = [0] * n
        cnt = 0
        for j in range(k):
            if (i >> j) & 1:
                ball[cd[j][0]-1] += 1
            else:
                ball[cd[j][1]-1] += 1
        for a, b in ab:
            if ball[a-1] and ball[b-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
