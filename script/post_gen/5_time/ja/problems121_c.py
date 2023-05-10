Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    drinks = []
    for i in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    ans = 0
    for i in range(n):
        if drinks[i][1] >= m:
            ans += drinks[i][0] * m
            break
        else:
            ans += drinks[i][0] * drinks[i][1]
            m -= drinks[i][1]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

main()

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        if m > b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A_B = [list(map(int,input().split())) for _ in range(N)]
    A_B.sort()
    ans = 0
    for i in range(N):
        if M > A_B[i][1]:
            ans += A_B[i][0]*A_B[i][1]
            M -= A_B[i][1]
        else:
            ans += A_B[i][0]*M
            break
    print(ans)

=======
Suggestion 5

def main():
    import sys
    readline = sys.stdin.readline

    N,M = map(int,readline().split())
    AB = [list(map(int,readline().split())) for _ in range(N)]
    AB.sort(key = lambda x:x[0])
    res = 0
    for a,b in AB:
        if M <= b:
            res += a * M
            break
        else:
            res += a * b
            M -= b
    print(res)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    a_b.sort()
    ans = 0
    for i in range(n):
        if m <= a_b[i][1]:
            ans += a_b[i][0] * m
            break
        else:
            ans += a_b[i][0] * a_b[i][1]
            m -= a_b[i][1]
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    ans = 0
    for a, b in AB:
        if b >= M:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b

    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    # print(n, m)
    # print(a[1], b[1])
    # print(a[0]*b[0])
    # print(a[0]*b[0]+a[1]*b[1])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]+a[4]*b[4])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]+a[4]*b[4]+a[5]*b[5])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]+a[4]*b[4]+a[5]*b[5]+a[6]*b[6])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]+a[4]*b[4]+a[5]*b[5]+a[6]*b[6]+a[7]*b[7])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]+a[4]*b[4]+a[5]*b[5]+a[6]*b[6]+a[7]*b[7]+a[8]*b[8])
    # print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if M == 0:
            break
        if M >= AB[i][1]:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
        else:
            ans += AB[i][0] * M
            M = 0
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())

    drinks = []
    for _ in range(n):
        a, b = map(int, input().split())
        drinks.append([a, b])

    drinks.sort(key=lambda x: x[0])

    ans = 0
    for drink in drinks:
        if m <= drink[1]:
            ans += drink[0] * m
            break
        else:
            ans += drink[0] * drink[1]
            m -= drink[1]

    print(ans)
