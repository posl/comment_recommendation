Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i] / B[i]
    ans /= 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #prin

=======
Suggestion 3

def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for a, b in ab:
        ans += a / b
    ans /= 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 二分探索
    left = 0
    right = 10**9 + 1
    while right - left > 10**(-5):
        mid = (right + left) / 2
        t = 0
        for i in range(N):
            t += (A[i] / mid) * B[i]
        if t >= 2:
            left = mid
        else:
            right = mid

    print(left)

=======
Suggestion 5

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    sumA = 0
    sumB = 0
    for i in range(N):
        sumA += AB[i][0] / AB[i][1]
        sumB += 1 / AB[i][1]
    print(sumA / sumB)

=======
Suggestion 6

def get_input():
    n = int(input())
    ab_list = []
    for _ in range(n):
        ab_list.append(list(map(int, input().split())))
    return n, ab_list

=======
Suggestion 7

def solve():
    N = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(N)]
    total_a = sum(a for a, b in AB)
    total_b = sum(b for a, b in AB)
    total_time = total_a / total_b

    time = 0
    for a, b in AB:
        time += a / b
        if time >= total_time / 2:
            print(time)
            break

=======
Suggestion 8

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    L = 0
    R = 100000000
    while R - L > 0.0000000001:
        M = (L + R) / 2
        t = 0
        for i in range(N):
            t += AB[i][0] / (AB[i][1] + M)
        if t >= M:
            L = M
        else:
            R = M
    print(L)

=======
Suggestion 9

def solve():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]
    #print(AB)
    #print(N)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])
    #print(AB[9][0])
    #print(AB[9][1])
    #print(AB[10][0])
    #print(AB[10][1])
    #print(AB[11][0])
    #print(AB[11][1])
    #print(AB[12][0])
    #print(AB[12][1])
    #print(AB[13][0])
    #print(AB[13][1])
    #print(AB[14][0])
    #print(AB[14][1])
    #print(AB[15][0])
    #print(AB[15][1])
    #print(AB[16][0])
    #print(AB[16][1])
    #print(AB[17][0])
    #print(AB[17][1])
    #print(AB[18][0])
    #print(AB[18][1])
    #print(AB[19][0])
    #print(AB[19][1])
    #print(AB[20][0])
    #print(AB[20][1])
    #print(AB[21][0])
    #print(AB[21][1])
    #print(AB[22][0])
    #print(AB[22][1])
    #print(

=======
Suggestion 10

def calcDistance(a, b):
    return a * b / (a + b)
