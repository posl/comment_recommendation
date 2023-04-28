Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    flame = 0
    for i in range(n):
        flame += a[i]/b[i]
    #print(flame)
    flame /= 2
    #print(flame)
    dist = 0
    for i in range(n):
        if flame > a[i]/b[i]:
            dist += a[i]
        else:
            dist += flame*b[i]
            break
    print(dist)

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i]/B[i]
    total /= 2
    dist = 0
    for i in range(N):
        if total >= A[i]/B[i]:
            total -= A[i]/B[i]
            dist += A[i]
        else:
            dist += B[i]*total
            break
    print(dist)
solve()

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    x = 0
    for i in range(N):
        x += A[i] / B[i]
    x /= 2

    y = 0
    for i in range(N):
        y += A[i] / B[i]
        if y >= x:
            print(x)
            return
    print(x)

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    t = 0
    for i in range(n):
        t += a[i] / b[i]
    t /= 2
    d = 0
    for i in range(n):
        if t >= a[i] / b[i]:
            d += a[i]
        else:
            d += b[i] * t
    print(d)

=======
Suggestion 5

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = A[::-1]
    B = B[::-1]
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
        right += A[i]
    right /= 2
    for i in range(N):
        if right >= A[i]:
            right -= A[i]
            left -= A[i] / B[i]
        else:
            left -= right / B[i]
            break
    return left


print(solve())

=======
Suggestion 6

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    l = 0
    r = 10**9
    while r - l > 10**(-6):
        m = (l + r) / 2
        if check(m, n, a, b):
            r = m
        else:
            l = m

    print(r)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.reverse()
    b.reverse()
    left = 0
    right = 10**10
    while right - left > 10**-5:
        mid = (left + right) / 2
        if check(n, a, b, mid):
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 8

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    time = 0
    for i in range(N):
        time += A[i] / B[i]
    time /= 2
    distance = 0
    for i in range(N):
        if time >= A[i] / B[i]:
            distance += A[i]
        else:
            distance += time * B[i]
    print(distance)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for a, b in AB:
        total += a / b
    total /= 2
    current = 0
    for a, b in AB:
        current += a / b
        if current >= total:
            print(current - (current - total) * b / a)
            break

=======
Suggestion 10

def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(input().split(' '))
    a_b = [[int(a_b[i][0]), int(a_b[i][1])] for i in range(n)]
    a_b = sorted(a_b, key=lambda x: x[0])
    time = 0
    for i in range(n):
        time += a_b[i][0] / a_b[i][1]
    half_time = time / 2
    distance = 0
    for i in range(n):
        if half_time > a_b[i][0] / a_b[i][1]:
            half_time -= a_b[i][0] / a_b[i][1]
            distance += a_b[i][0]
        else:
            distance += half_time * a_b[i][1]
            break
    print(distance)
