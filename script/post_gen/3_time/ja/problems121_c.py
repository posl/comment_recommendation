Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append((a[i], b[i]))
    c.sort()
    #print(c)
    ans = 0
    for i in range(n):
        if m >= c[i][1]:
            ans += c[i][0] * c[i][1]
            m -= c[i][1]
        else:
            ans += c[i][0] * m
            break
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # AとBを結合して、Aの昇順、Bの昇順にソートする。
    AB = sorted(zip(A, B))
    # print(AB)
    # 合計金額
    total = 0
    # 購入済みの本数
    count = 0
    for a, b in AB:
        if count + b < M:
            total += a * b
            count += b
        else:
            total += a * (M - count)
            break
    print(total)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort()
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

def solve():
    n, m = map(int, input().split())
    drinks = []
    for i in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    count = 0
    price = 0
    for drink in drinks:
        if count + drink[1] <= m:
            count += drink[1]
            price += drink[0] * drink[1]
        else:
            price += drink[0] * (m - count)
            break
    print(price)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    drink = []
    for i in range(n):
        a, b = map(int, input().split())
        drink.append((a, b))
    drink.sort()
    ans = 0
    for i in range(n):
        if m >= drink[i][1]:
            ans += drink[i][0] * drink[i][1]
            m -= drink[i][1]
        else:
            ans += drink[i][0] * m
            m -= m
        if m == 0:
            break
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
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
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if ab[i][1] >= m:
            ans += ab[i][0] * m
            m = 0
        else:
            ans += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    shop = []
    for i in range(n):
        a,b = map(int,input().split())
        shop.append([a,b])
    shop.sort()
    ans = 0
    for i in range(n):
        if m <= 0:
            break
        if m >= shop[i][1]:
            ans += shop[i][0] * shop[i][1]
            m -= shop[i][1]
        else:
            ans += shop[i][0] * m
            m = 0
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if AB[i][1] < M:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
        else:
            ans += AB[i][0] * M
            break
    print(ans)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    cnt = 0
    for a,b in ab:
        if cnt + b < m:
            ans += a*b
            cnt += b
        else:
            ans += a*(m-cnt)
            break
    print(ans)
