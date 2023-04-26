Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i == j:
                continue
            if A[i] > A[j]:
                tmp += A[i] - A[j]
            else:
                tmp += A[j] - A[i]
        if ans < tmp:
            ans = tmp
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        total = 0
        for j in range(n):
            total += a[(i+j) % n]
            if total > max:
                max = total
    print(max)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = 360 * (n - 2) - ans
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(a[0])
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] - a[i+1])
    print(360 - ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    max_angle = 0
    for i in range(n):
        angle = abs(a[i] - a[i+1])
        if angle > 180:
            angle = 360 - angle
        max_angle = max(max_angle, angle)
    print(360-max_angle)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a * 2
    max = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += a[i+j]
            if tmp > max:
                max = tmp
    print(360-max)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    max = 0
    for i in range(1, n+1):
        diff = a[i] - a[i-1]
        if diff > max:
            max = diff
    print(360 - max)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%360 for i in a]

    max = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += a[(i+j)%n]
            if sum > max:
                max = sum

    print(max)

=======
Suggestion 9

def calc_max_angle(n, angles):
    angles.sort(reverse=True)
    angles.append(360 + angles[0])
    max_angle = 0
    for i in range(n):
        max_angle = max(max_angle, angles[i] - angles[i+1])
    return max_angle

=======
Suggestion 10

def solve(n, a):
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = 360 - ans
    return ans
