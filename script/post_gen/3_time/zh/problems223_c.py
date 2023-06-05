Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # print(a)
    # print(b)

    # 两个火焰相遇的时间
    t = sum(a) / sum(b)
    # print(t)

    # 两个火焰相遇的位置
    x = 0
    for i in range(n):
        x += a[i] / b[i]
        if x >= t / 2:
            break
    # print(x)

    # 相遇的位置与物体左端之间的距离
    y = 0
    for i in range(n):
        y += a[i]
        if y >= x * b[i]:
            break
    print(y)

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        temp = input().split()
        a.append(int(temp[0]))
        b.append(int(temp[1]))
    left = 0
    right = 0
    for i in range(n):
        left += a[i] / b[i]
    left /= 2
    for i in range(n):
        if left - a[i] / b[i] > 0:
            left -= a[i] / b[i]
        else:
            right += a[i] / b[i] - left
            left = 0
    print(right)

=======
Suggestion 3

def get_distance(a, b):
    return a / (a + b) * a

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
    # print(A)
    # print(B)
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
        right += A[N - i - 1] / B[N - i - 1]
    print(left / 2 + right / 2)

=======
Suggestion 5

def distance(a, b, c, d):
    return (a * c + b * d) / (b + d)

=======
Suggestion 6

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    #print(N, AB)
    #print(AB[0])
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[0][0] / AB[0][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1] + AB[2][0] / AB[2][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1] + AB[2][0] / AB[2][1] + AB[3][0] / AB[3][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1] + AB[2][0] / AB[2][1] + AB[3][0] / AB[3][1] + AB[4][0] / AB[4][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1] + AB[2][0] / AB[2][1] + AB[3][0] / AB[3][1] + AB[4][0] / AB[4][1] + AB[5][0] / AB[5][1])
    #print(AB[0][0] / AB[0][1] + AB[1][0] / AB[1][1] + AB[2][0] / AB[2][1] + AB[3][0] / AB[3][1] + AB[4][0] / AB[4][1] + AB[5][0] / AB[5][1] + AB[6][0] / AB[6][1])
    #print(AB[0][0] / AB[0][1] + AB[1][

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum_a = sum(a)
    sum_b = sum([a_i / b_i for a_i, b_i in zip(a, b)])
    #print(sum_a, sum_b)
    sum_a_b = sum_a / sum_b
    sum_a_b_i = 0
    for i in range(n):
        sum_a_b_i += a[i] / b[i]
        if sum_a_b_i >= sum_a_b:
            print(sum_a_b_i)
            break

=======
Suggestion 8

def getMeetPoint(A,B):
    # A: 保险丝长度
    # B: 保险丝燃烧速度
    # 返回两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的时间为：x = (A1+A2)/(B1+B2)
    # 两个火焰相遇的位置为：y = (A1*B2+A2*B1)/(B1+B2)
    # 两个火焰相遇后，火焰1燃烧的距离为：A1-B1*x
    # 两个火焰相遇后，火焰2燃烧的距离为：A2-B2*x
    # 因此两个火焰相遇后，火焰1燃烧的距离与火焰2燃烧的距离相等
    # 即：A1-B1*x = A2-B2*x
    # 解得：x = (A1-A2)/(B1-B2)
    # y = (A1*B2-A2*B1)/(B1-B2)
    # 若x>0，则两个火焰相遇的位置在物体的右侧，此时两个火焰相遇的位置与物体左端之间的距离为：y
    # 若x<0，则两个火焰相遇的位置在物体的左侧，此时两个火焰相遇的位置与物体左端之间的距离为：A1
    # 若x=0，则两个火焰相遇的位置在物体的左端，此时两个火焰相遇的位置与物体左端之间的距离为：0
    # 若x=0，则两个火焰相遇的位置在物体的右端，此时两个火焰相遇的位置与物体左端之

=======
Suggestion 9

def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += a[i] / b[i]
    ans /= 2
    for i in range(n):
        ans -= a[i] / b[i]
        if ans < 0:
            ans += a[i] / b[i]
            break
    print(ans)


solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-i-1]/B[N-i-1]
    print(left + right)
