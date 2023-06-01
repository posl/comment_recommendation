Synthesizing 9/10 solutions

=======
Suggestion 1

def getDistance(a, b, n):
    # a: length of wire
    # b: burning speed
    # n: number of wires
    # return: distance between two fires
    # the distance between two fires is determin

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-1-i]/B[N-1-i]
    ans = 0
    for i in range(N):
        ans += A[i]*(left-right)/2
        left -= A[i]/B[i]
        right += A[N-1-i]/B[N-1-i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    #print(a)
    #print(b)
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(a[0] + a[1])
        return
    total = 0
    for i in range(n):
        total += a[i] / b[i]
    #print(total)
    half = total / 2
    #print(half)
    for i in range(n):
        if half < a[i] / b[i]:
            print(half * b[i])
            return
        half -= a[i] / b[i]
    print(total - half)

=======
Suggestion 4

def solve(n, ab):
    s = 0
    for a, b in ab:
        s += a / b
    t = s / 2
    s = 0
    for a, b in ab:
        if a / b < t:
            s += a
        else:
            s += t * b
            break
    return s

=======
Suggestion 5

def calc_distance(a, b):
    return float(a) / (a + b)

=======
Suggestion 6

def cal_distance(AB):
    N = len(AB)
    if N == 1:
        return AB[0][0]
    else:
        left = AB[0][0]
        right = AB[N-1][0]
        while left < right:
            mid = (left + right) / 2
            sum = 0
            for i in range(N):
                if mid < AB[i][0]:
                    sum += AB[i][0] - mid
            if sum == mid:
                return mid
            elif sum > mid:
                left = mid
            else:
                right = mid

N = int(raw_input())
AB = []
for i in range(N):
    AB.append(map(int, raw_input().split()))
AB.sort()
print cal_distance(AB)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = input().split()
        a.append(int(ai))
        b.append(int(bi))

    # print(a)
    # print(b)

    # 从左到右
    left = 0
    for i in range(n):
        left += a[i]
    # print(left)

    # 从右到左
    right = 0
    for i in range(n):
        right += a[n - 1 - i]
    # print(right)

    # 从左到右
    left_speed = 0
    for i in range(n):
        left_speed += b[i]
    # print(left_speed)

    # 从右到左
    right_speed = 0
    for i in range(n):
        right_speed += b[n - 1 - i]
    # print(right_speed)

    # 两团火焰将在距离物体左端3厘米处相遇。
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间

    # 两个火焰相遇的时间
    t = left / (left_speed + right_speed)
    # print(t)

    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇

=======
Suggestion 8

def get_distance(a, b, n):
    """
    二分法
    :param a: a
    :param b: b
    :param n: n
    :return: distance
    """
    left = 0
    right = 1000
    while left < right:
        mid = (left + right) / 2
        sum = 0
        for i in range(n):
            sum += a[i] / (mid - b[i])
        if sum < 1:
            right = mid
        else:
            left = mid
    return left

=======
Suggestion 9

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = sum(A)
    half = total / 2
    time = 0
    for i in range(N):
        time += A[i] / B[i]
        if time >= half:
            print(half * 2 - total)
            break
