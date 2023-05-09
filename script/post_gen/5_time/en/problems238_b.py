Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]
    ans = abs(ans)
    ans = min(ans, 360 - ans)
    print(ans)
    return

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    ans = 0
    for i in range(n+1):
        ans = max(ans, (a[i+1]-a[i])%360)
    print(360-ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] - 180
    print(abs(ans))

=======
Suggestion 4

def find_center_angle(angles):
    angles.sort()
    angles.append(360+angles[0])
    max_angle = 0
    for i in range(len(angles)-1):
        angle = angles[i+1] - angles[i]
        if angle > max_angle:
            max_angle = angle
    return 360 - max_angle

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max = 0
    for i in range(n):
        for j in range(i,n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n-1):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    if max < 360 - a[n-1] + a[0]:
        max = 360 - a[n-1] + a[0]
    print(360 - max)

=======
Suggestion 6

def main():
    # Get input here
    n = int(input())
    a = list(map(int, input().split()))

    # Calculate result here
    ans = 0
    for i in range(n):
        ans += a[i]

    # Print output here
    print(360 - ans)

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    angle = 360 / n
    ans = 0
    for i in range(n):
        ans = max(ans, sum(a[i:]) + sum(a[:i]) + angle * (n - 1))
    print(int(360 - ans))

=======
Suggestion 8

def get_max_angle(angles):
    angles.sort()
    angles.reverse()
    angles.append(angles[0] + 360)
    max_angle = 0
    for i in range(len(angles)-1):
        angle = angles[i] - angles[i+1]
        if angle > max_angle:
            max_angle = angle
    return max_angle

=======
Suggestion 9

def solve(N, A):
    #print(N, A)
    maxA = 0
    for i in range(N):
        A[i] = A[i] % 360
        maxA = max(maxA, A[i])
    #print(A)
    A.sort()
    #print(A)
    maxA = max(maxA, 360-A[N-1]+A[0])
    for i in range(1, N):
        maxA = max(maxA, A[i]-A[i-1])
    return 360-maxA

=======
Suggestion 10

def main():
    print("Hello World!")
    return
