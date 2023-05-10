Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += a[i]/b[i]
    ans /= 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 10**18
    while right - left > 10**(-6):
        mid = (left + right) / 2
        t = 0
        for i in range(N):
            t += (mid - A[i]) / B[i]
        if t < mid:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 3

def get_input_int():
    return int(input())

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

    # 着火前の導火線の長さ
    L = sum(A)

    # 着火前の導火線の左端からの距離
    # 火がぶつかる場所の左側の距離を求める
    # この距離を求めるために、火がぶつかる場所の右側の距離を求める
    # 火がぶつかる場所の右側の距離を求めるために、火がぶつかる場所の右側の時間を求める
    # 火がぶつかる場所の右側の時間を求めるために、火がぶつかる時間を求める
    # 火がぶつかる時間を求めるために、火がぶつかる場所を求める
    # 火がぶつかる場所を求めるために、火がぶつかる場所の左側の距離を求める
    # 火がぶつかる場所の左側の距離を求めるために、火がぶつかる場所の左側の時間を求める
    # 火がぶつかる場所の左側の時間を求めるために、火がぶつかる時間を求める
    # 火がぶつかる時間を求めるために、火がぶつかる場所を求める
    # 火がぶつかる場所を求めるために、火がぶつかる場所の左側の距離を求める
    #

=======
Suggestion 5

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
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
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    A = 0
    B = 0
    for i in range(N):
        A += AB[i][0]/AB[i][1]
        B += 1/AB[i][1]

    print(A/B)

=======
Suggestion 7

def calc(n, a, b):
    s = 0
    for i in range(n):
        s += a[i] / b[i]
    s /= 2
    t = 0
    for i in range(n):
        t += a[i] / b[i]
        if t >= s:
            return t
    return s

n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

print(calc(n, a, b))

=======
Suggestion 8

def get_input_data():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    return N,A,B

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    ans = 0
    for i in range(N):
        ans += A[i]/B[i]
    ans /= 2
    print(ans)

=======
Suggestion 10

def calc_time(a, b):
    return a / b
