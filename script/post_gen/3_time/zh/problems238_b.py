Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_max_angle(n, angles):
    angles.sort()
    angles.append(angles[0] + 360)
    max_angle = 0
    for i in range(n):
        angle = angles[i + 1] - angles[i]
        if angle > max_angle:
            max_angle = angle
    return 360 - max_angle

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def get_max_angle(num, data):
    max_angle = 0
    for i in range(num):
        angle = 0
        for j in range(num):
            angle += data[(j+i)%num]
            if angle > 180:
                angle = 360 - angle
            if angle > max_angle:
                max_angle = angle
    return max_angle

=======
Suggestion 4

def findMaxAngle(angles):
    maxAngle = 0
    for i in range(len(angles)):
        angle = angles[i]-angles[0]
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle
        if angle > maxAngle:
            maxAngle = angle
    return maxAngle

=======
Suggestion 5

def get_max_angle(N, A):
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(i + j) % N]
            if angle > max_angle:
                max_angle = angle
    return max_angle

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

def calMaxAngle(N, A):
    maxAngle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            if i == j:
                continue
            if A[i] > A[j]:
                angle += (A[i] - A[j])
            else:
                angle += (360 - A[j] + A[i])
        if maxAngle < angle:
            maxAngle = angle
    return maxAngle

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(A[0]+360)
    max = 0
    for i in range(N):
        if A[i+1]-A[i] > max:
            max = A[i+1]-A[i]
    print(360-max)
