Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a[i] = a[i] % 360
    a.sort()
    for i in range(n):
        a.append(a[i] + 360)
    for i in range(n):
        ans = max(ans, a[i+n-1] - a[i])
    print(360 - ans)

=======
Suggestion 2

def problem238b():
    pass

=======
Suggestion 3

def max_angle(N, A):
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(i+j)%N]
            if max_angle < angle:
                max_angle = angle
    return max_angle

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(A[0]+360)
    max = 0
    for i in range(N):
        if max < A[i+1] - A[i]:
            max = A[i+1] - A[i]
    print(360 - max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        now = 0
        for j in range(n):
            now += a[(i + j) % n]
            result = max(result, now)
    print(360 - result)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0]+360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i+1]-a[i])
    print(360-ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    A.append(A[0]+360)
    max = 0
    for i in range(N):
        if max < A[i+1]-A[i]:
            max = A[i+1]-A[i]
    print(360-max)

=======
Suggestion 8

def main():
    #读取输入
    n = int(input())
    a = list(map(int, input().split()))
    #计算最大值
    max = 0
    for i in range(n):
        #计算角度
        angle = 360.0 / 2.0 - a[i]
        #如果角度大于180，就用360减去角度
        if(angle > 180):
            angle = 360 - angle
        #如果角度大于max，就更新max
        if(angle > max):
            max = angle
    #打印结果
    print(int(max))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(j + i) % N]
            max_angle = max(max_angle, min(angle, 360 - angle))

    print(360 - max_angle)
