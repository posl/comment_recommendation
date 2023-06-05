Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    s = sum(a[:3])
    ans = s
    for i in range(n-3):
        s += a[i+3]
        s -= a[i]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.append(a[0])
    a.append(a[1])
    sum = 0
    for i in range(n):
        sum += abs(a[i+1] - a[i])
    print(sum)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i]
    print(ans)
solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    for i in range(2 * N - 1):
        A[i + 1] += A[i]
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + N - 1] - A[i])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(0)

    # 从a[0]开始，逆时针方向的最大值
    left = [0] * (n + 2)
    # 从a[n-1]开始，顺时针方向的最大值
    right = [0] * (n + 2)

    for i in range(n):
        left[i + 1] = max(left[i], a[i])
        right[n - i] = max(right[n - i + 1], a[n - i - 1])

    ans = 0
    for i in range(n):
        ans = max(ans, a[i] + min(left[i], right[i + 2]))

    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1, N):
        ans += A[i] * (i + 1)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += a[i]
        else:
            ans += min(a[i], a[i-1])
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    for i in range(n):
        a[i] += a[i+1]
    a.append(a[2])
    ans = 0
    for i in range(n):
        ans = max(ans, min(a[i], a[i+n]))
    print(ans)

=======
Suggestion 10

def maxComfort(n, a):
    a.append(a[0])
    a.append(a[1])
    max_comfort = 0
    comfort = 0
    for i in range(1, n+1):
        comfort += min(a[i-1], a[i+1])
        max_comfort = max(max_comfort, comfort)
        if comfort < 0:
            comfort = 0
    return max_comfort
