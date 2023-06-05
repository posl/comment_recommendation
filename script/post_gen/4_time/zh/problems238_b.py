Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.append(a[0] + 360)
    a.append(a[1] + 360)
    max = 0
    for i in range(n):
        if a[i + 2] - a[i] > max:
            max = a[i + 2] - a[i]
    print(360 - max)

=======
Suggestion 2

def get_max_angle(N, A):
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(i + j) % N]
            if angle > 180:
                angle = 360 - angle
            if angle > max_angle:
                max_angle = angle
    return max_angle

=======
Suggestion 3

def get_max_angle(n, angles):
    result = 0
    for i in range(n):
        angle = angles[i]
        temp = angle
        for j in range(n):
            if j == i:
                continue
            temp += angles[j]
            temp %= 360
        if temp > result:
            result = temp
    return result

=======
Suggestion 4

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 从第一个角开始旋转
    ans = 0
    for i in range(n):
        # 记录角度
        deg = 0
        for j in range(n):
            # 每次旋转角度
            if i != j:
                # 逆时针旋转
                x = a[j] - a[i]
                if x < 0:
                    x += 360
                deg = max(deg, x)
        # 记录最大角度
        ans = max(ans, deg)
    # 输出
    print(ans)

=======
Suggestion 5

def solve(n, a):
    max_angle = 0
    for i in range(n):
        total_angle = 0
        for j in range(n):
            total_angle += a[(i + j) % n]
            if total_angle > 180:
                total_angle = 360 - total_angle
            if total_angle > max_angle:
                max_angle = total_angle
    return max_angle

=======
Suggestion 6

def pizza_cut(n, a):
    """切割比萨饼"""
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = max(ans, abs(a[i] - a[j]))
            ans = max(ans, 360 - abs(a[i] - a[j]))
    return ans

=======
Suggestion 7

def get_max_angle(n, angles):
    # 以一个圆的圆心为原点，建立直角坐标系
    # 每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 因此，每次切割都是在圆上的某一点与圆心连线上的垂线
    # 每次切割都是在圆上的某一点与圆心连线上的垂线
    # 每次切割都是在圆上的某一点与圆心连线上的垂线
    # 每次切割都是在圆上的某一点与圆心连线上的垂线
    angles.sort()
    angles.append(angles[0] + 360)
    max_angle = 0
    for i in range(n):
        angle = angles[i+1] - angles[i]
        if angle

=======
Suggestion 8

def get_max_angle(A):
    N = len(A)
    max_angle = 0
    for i in range(N):
        angle = A[i]
        if angle > max_angle:
            max_angle = angle
    return max_angle

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(360 - a[0])
    else:
        max_angle = 0
        for i in range(n):
            for j in range(i, n):
                angle = a[j] - a[i]
                if angle < 0:
                    angle += 360
                max_angle = max(max_angle, angle)
        print(360 - max_angle)

=======
Suggestion 10

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
