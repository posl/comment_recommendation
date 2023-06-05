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
    bsum = sum(b)
    if m <= bsum:
        print(sum([a[i]*b[i] for i in range(n) if m > 0]))
    else:
        print(sum([a[i]*b[i] for i in range(n)]) + a[b.index(min(b))]*(m-bsum))

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
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

solve()

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    count = 0
    ans = 0
    for i in range(n):
        if count + ab[i][1] < m:
            ans += ab[i][0] * ab[i][1]
            count += ab[i][1]
        else:
            ans += ab[i][0] * (m - count)
            break
    print(ans)

=======
Suggestion 4

def solve():
    # 读入数据
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        A, B = map(int, input().split())
        data.append((A, B))
    # 按照单价从小到大排序
    data.sort()
    # 依次购买能量饮料
    ans = 0
    rest = M
    for i in range(N):
        # 优先购买单价低的
        if rest >= data[i][1]:
            ans += data[i][0] * data[i][1]
            rest -= data[i][1]
        else:
            ans += data[i][0] * rest
            rest = 0
        if rest == 0:
            break
    print(ans)

=======
Suggestion 5

def min_money(n, m, list):
    list.sort(key=lambda x: (x[0], -x[1]))
    i = 0
    money = 0
    while m > 0:
        if list[i][1] >= m:
            money += m * list[i][0]
            break
        else:
            money += list[i][1] * list[i][0]
            m -= list[i][1]
            i += 1
    print(money)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        if M == 0:
            break
        if B[i] >= M:
            ans += A[i] * M
            M = 0
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a_b = list(zip(a,b))
    a_b.sort()
    sum_b = 0
    sum_money = 0
    for i in range(n):
        if sum_b + a_b[i][1] <= m:
            sum_b += a_b[i][1]
            sum_money += a_b[i][0] * a_b[i][1]
        else:
            sum_money += a_b[i][0] * (m - sum_b)
            break
    print(sum_money)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    l = []
    for i in range(N):
        a, b = map(int, input().split())
        l.append((a, b))
    l.sort()
    s = 0
    for a, b in l:
        if M <= b:
            s += a * M
            break
        s += a * b
        M -= b
    print(s)

=======
Suggestion 9

def getMinPrice(n, m, stores):
    # stores.sort(key = lambda x: x[0]/x[1])
    # print(stores)
    stores.sort(key = lambda x: x[0])
    # print(stores)
    # print(stores[0][0])
    # print(stores[0][1])
    count = 0
    price = 0
    for i in range(n):
        if count >= m:
            break
        if count + stores[i][1] >= m:
            price += (m - count) * stores[i][0]
            count += (m - count)
        else:
            price += stores[i][1] * stores[i][0]
            count += stores[i][1]
    return price

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    shop = []
    for i in range(n):
        shop.append(list(map(int, input().split())))
    shop.sort(key=lambda x: x[0])
    count = 0
    for i in range(n):
        if shop[i][1] >= m:
            count += shop[i][0] * m
            return count
        else:
            count += shop[i][0] * shop[i][1]
            m -= shop[i][1]
