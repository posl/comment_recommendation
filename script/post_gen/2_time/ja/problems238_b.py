Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 10
    a = [215, 137, 320, 339, 341, 41, 44, 18, 241, 149]
    # n = 1
    # a = [1]
    # n = 4
    # a = [90, 180, 45, 195]
    # n = 5
    # a = [90, 180, 45, 195, 90]
    # n = 6
    # a = [90, 180, 45, 195, 90, 90]
    # n = 7
    # a = [90, 180, 45, 195, 90, 90, 90]
    # n = 8
    # a = [90, 180, 45, 195, 90, 90, 90, 90]
    # n = 9
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90]
    # n = 10
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90, 90]
    # n = 359
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90, 90]
    # n = 360
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90, 90]
    # n = 361
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90, 90]
    # n = 362
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90, 90]
    # n = 363
    # a = [90, 180, 45, 195, 90, 90, 90, 90, 90,

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += a_list[(i+j)%n]
            max_angle = max(max_angle, angle)
    print(360-max_angle)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    print(360 - ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        a_sum = 0
        for j in range(n):
            if i == j:
                continue
            a_sum += a[j]
            if a_sum >= 360:
                a_sum -= 360
        if a_sum > max:
            max = a_sum
    print(max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%360 for i in a]
    a.sort()
    a.append(a[0]+360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i+1]-a[i])
    print(360-ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    max_angle = 0
    for i in range(n):
        max_angle = max(max_angle, a[i+2]-a[i])
    print(360-max_angle)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i%360 for i in A]
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            if j <= i:
                angle += A[j]
            else:
                angle -= A[j]
        if angle > max_angle:
            max_angle = angle
    print(max_angle)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0])
    max = 0
    for i in range(n):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    print(360 - max)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(N):
        A[i] = 360 - A[i]
    #print(A)
    for i in range(N):
        for j in range(i+1, N):
            A[i] = A[i] % A[j]
    print(A[0])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A

    # print(N)
    # print(A)

    # 1回目の切断
    # 2回目以降の切断
    # 2回目以降の切断は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何度か
    # 2回目以降の切断位置は、1回目の切断位置からの相対角度で表現する
    # 1回目の切断位置は、12時の方向に対して何
