Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.append(a[0] + 360)
    a.append(a[1] + 360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 2] - a[i])
    print(360 - ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0]+360)
    a.append(a[1]+360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i+2]-a[i])
    print(360-ans)

=======
Suggestion 3

def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + 360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 1] - a[i])
    print(360 - ans)
    return 0

func()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            ans = max(ans, sum)
    print(ans)

=======
Suggestion 5

def get_max_angle(n, angles):
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += angles[(i+j)%n]
            if angle > max_angle:
                max_angle = angle
    return max_angle

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a.append(a[0]+360)
    max = 0
    for i in range(n):
        if a[i+1] - a[i] > max:
            max = a[i+1] - a[i]
    print(360 - max)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(1, n):
        if a[i] - a[i-1] < 0:
            a[i] += 360
    a.sort()
    for i in range(n):
        ans = max(ans, a[i] - a[i-1])
    print(360 - ans)

=======
Suggestion 8

def max_angle(n, angle_list):
    angle_list.sort()
    max_angle = 0
    for i in range(n):
        angle = angle_list[i] - angle_list[i-1]
        if angle > max_angle:
            max_angle = angle
    return max_angle

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += a[(i + j) % n]
            if angle > 180:
                angle = 360 - angle
            max_angle = max(max_angle, angle)
    print(360 - max_angle)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.append(a[0] + 360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i+1] - a[i])
    print(360 - ans)
