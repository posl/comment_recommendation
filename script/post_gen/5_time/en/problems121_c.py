Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    drinks = []
    for i in range(N):
        drinks.append([A[i], B[i]])
    drinks.sort()
    price = 0
    num = M
    for i in range(N):
        if num >= drinks[i][1]:
            price += drinks[i][0] * drinks[i][1]
            num -= drinks[i][1]
        else:
            price += drinks[i][0] * num
            break
    print(price)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    #print(n, m)
    #print(a)
    #print(b)

    #a = [4, 2]
    #b = [9, 4]
    #m = 5
    #n = 2
    #a = [6, 2, 3, 7]
    #b = [18, 5, 10, 9]
    #m = 30
    #n = 4
    #a = [1000000000]
    #b = [100000]
    #m = 100000
    #n = 1

    #a = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #b = [100000, 100000, 100000, 100000, 100000]
    #m = 100000
    #n = 5

    #a = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #b = [100000, 100000, 100000, 100000, 100000]
    #m = 100000
    #n = 5

    #a = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #b = [100000, 100000, 100000, 100000, 100000]
    #m = 100000
    #n = 5

    #a = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #b = [100000, 100000, 100000, 100000, 100000]
    #m = 100000
    #n = 5

    #a = [1000000000, 1000000000, 1000000000, 100000000

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        ans += a * min(m, b)
        m -= min(m, b)
        if m == 0:
            break
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if M > 0:
            if M >= AB[i][1]:
                ans += AB[i][0] * AB[i][1]
                M -= AB[i][1]
            else:
                ans += AB[i][0] * M
                M -= M
        else:
            break
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
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
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    return n, m, a, b

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(N)]
    store.sort()
    ans = 0
    for i in range(N):
        if M > store[i][1]:
            ans += store[i][0] * store[i][1]
            M -= store[i][1]
        else:
            ans += store[i][0] * M
            break
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    drink = []
    for i in range(n):
        drink.append(list(map(int, input().split())))
    drink.sort()
    ans = 0
    for i in range(n):
        if drink[i][1] >= m:
            ans += drink[i][0] * m
            break
        else:
            ans += drink[i][0] * drink[i][1]
            m -= drink[i][1]
    print(ans)

=======
Suggestion 9

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = deque()
    B = deque()
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    while M > 0:
        a = A.popleft()
        b = B.popleft()
        if M > b:
            ans += a * b
            M -= b
        else:
            ans += a * M
            M = 0
    print(ans)

=======
Suggestion 10

def min_cost(n, m, a_b):
    a_b = sorted(a_b, key=lambda x: x[0])
    cost = 0
    for a, b in a_b:
        if m <= b:
            cost += m * a
            break
        else:
            cost += a * b
            m -= b
    return cost
