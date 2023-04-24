Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    l = 0
    r = 1000000000000
    while r - l > 0.0000000000001:
        m = (l + r) / 2
        t = 0
        for i in range(N):
            t += max(0, A[i] - m / B[i])
        if t >= m:
            l = m
        else:
            r = m
    print(l)
solve()

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 0
    for i in range(n):
        ans += a[i]/b[i]
    ans /= 2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i]/B[i]
    sum /= 2
    ans = 0
    for i in range(N):
        sum -= A[i]/B[i]
        if sum < 0:
            ans += A[i] + sum*B[i]
            break
        ans += A[i]
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = B = 0
    for i in range(N):
        a, b = map(int, input().split())
        A += a / b
        B += 1 / b
    return A / B

print(solve())

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    total = 0
    for i in range(n):
        total += a[i]/b[i]
    total /= 2
    distance = 0
    for i in range(n):
        if total < a[i]/b[i]:
            distance += total * b[i]
            break
        else:
            distance += a[i]
            total -= a[i]/b[i]
    print(distance)

main()

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    left = 0
    right = 100000
    while right - left > 0.0000000001:
        mid = (left + right) / 2
        #print("left: %f, right: %f, mid: %f" % (left, right, mid))
        t = 0
        for i in range(N):
            t = t + A[i] / (B[i] + mid)
        #print("t: %f" % t)
        if t < mid:
            right = mid
        else:
            left = mid
    print(mid)

=======
Suggestion 7

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for a,b in AB:
        ans += a/b
    ans /= 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    time = 0
    for i in range(N):
        time += AB[i][0] / AB[i][1]
    time /= 2
    dist = 0
    for i in range(N):
        if time >= AB[i][0] / AB[i][1]:
            dist += AB[i][0]
        else:
            dist += AB[i][1] * time
    print(dist)

=======
Suggestion 9

def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int, input().split())))

    total_a = 0
    total_b = 0
    for i in range(n):
        total_a += a_b[i][0] / a_b[i][1]
        total_b += 1 / a_b[i][1]

    print(total_a / total_b)

=======
Suggestion 10

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    left = 0
    right = 0
    for a, b in AB:
        left += a / b
        right += a / b
    right -= AB[-1][0] / AB[-1][1]
    while right - left > 0.0000000001:
        mid = (right + left) / 2
        left_sum = 0
        for a, b in AB:
            left_sum += max(0, a - mid * b) / b
        if left_sum > mid:
            left = mid
        else:
            right = mid
    print(left)
