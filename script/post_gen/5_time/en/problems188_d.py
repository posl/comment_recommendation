Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        events.append((a-1, c))
        events.append((b, -c))
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        ans += min(C, fee) * (x - t)
        fee += y
        t = x
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(N):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    a.sort()
    b.sort()
    c.sort()
    total = 0
    i = 0
    j = 0
    k = 0
    while i < N:
        while j < N and a[j] <= b[i]:
            j += 1
        total += C * (j - k)
        k = j
        while k < N and b[k] < a[i]:
            k += 1
        total += c[i] * (k - j)
        i += 1
    print(total)

=======
Suggestion 3

def main():
    n, c = map(int, input().split())
    l = []
    for i in range(n):
        a, b, c = map(int, input().split())
        l.append([a, c])
        l.append([b + 1, -c])
    l.sort()
    ans = 0
    fee = 0
    t = 0
    for i in range(2 * n):
        if l[i][0] != t:
            ans += min(c, fee) * (l[i][0] - t)
            t = l[i][0]
        fee += l[i][1]
    print(ans)

=======
Suggestion 4

def main():
    n, c = map(int, input().split())
    s = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        s.append((a, c))
        s.append((b + 1, -c))
    s.sort()
    ans = 0
    t = 0
    for i in range(2 * n):
        if i > 0:
            ans += min(c, t) * (s[i][0] - s[i - 1][0])
        t += s[i][1]
    print(ans)

=======
Suggestion 5

def main():
    n, c = map(int, input().split())
    a = []
    b = []
    cost = []
    for i in range(n):
        a_, b_, c_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
        cost.append(c_)
    #print(a)
    #print(b)
    #print(cost)
    #print('----------------')
    #a = [1, 2]
    #b = [2, 2]
    #cost = [4, 4]
    #c = 6
    #n = 2
    #print(a)
    #print(b)
    #print(cost)
    #print('----------------')
    #a = [583563238, 136809000, 54601291, 5797762, 468677897]
    #b = [820642330, 653199778, 785892285, 453599267, 916692569]
    #cost = [44577, 90962, 50554, 65697, 87409]
    #c = 1000000000
    #n = 5
    #print(a)
    #print(b)
    #print(cost)
    #print('----------------')
    #a = [583563238, 136809000, 54601291, 5797762, 468677897]
    #b = [820642330, 653199778, 785892285, 453599267, 916692569]
    #cost = [44577, 90962, 50554, 65697, 87409]
    #c = 100000
    #n = 5
    #print(a)
    #print(b)
    #print(cost)
    #print('----------------')
    #a = [583563238, 136809000, 54601291, 5797762, 468677897]
    #b = [820642330, 653199778, 785892285, 453599267, 916692569]
    #cost = [44577, 90962, 50554, 65697, 87409]
    #c = 100000
    #n = 5
    #print(a)
    #print(b)
    #print(cost)

=======
Suggestion 6

def main():
    n, c = map(int, input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        a.append(0)
        b.append(0)
        d.append(0)
    for i in range(n):
        a[i], b[i], d[i] = map(int, input().split())
    s = 0
    e = 0
    p = 0
    for i in range(n):
        s = a[i]
        e = b[i] + 1
        p = d[i]
        d[i] = 0
        for j in range(s, e):
            d[j - 1] += p
    m = max(d)
    if m > c:
        print(c)
    else:
        print(m)

=======
Suggestion 7

def main():
    n, c = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]
    abc.sort(key=lambda x: x[0])
    abc.sort(key=lambda x: x[2])

    total = 0
    day = 0
    fee = 0
    for a, b, c in abc:
        if day == a and fee == c:
            continue
        total += (a - day) * min(c, fee)
        day = a
        fee = c
        total += c * (b - a + 1)
        day = b + 1

    print(total)

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]

    # 2N個のイベントを作る
    # 2N個のイベントをソートする
    # 2N個のイベントを順番に見ていき、イベントの種類に応じて処理する
    # その都度、支払い金額を計算する
    # その都度、最小支払い金額を更新する

    events = []
    for i in range(N):
        a, b, c = abc[i]
        events.append([a - 1, c])
        events.append([b, -c])
    events.sort()

    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)

=======
Suggestion 9

def solve():
    N, C = map(int, input().split())
    # print(N, C)
    # print(type(N), type(C))

    # a, b, c = [], [], []
    # for i in range(N):
    #     _a, _b, _c = map(int, input().split())
    #     a.append(_a)
    #     b.append(_b)
    #     c.append(_c)
    # print(a, b, c)

    # N, C = 5, 1000000000
    # a = [583563238, 136809000, 54601291, 5797762, 468677897]
    # b = [820642330, 653199778, 785892285, 453599267, 916692569]
    # c = [44577, 90962, 50554, 65697, 87409]
    # N, C = 5, 100000
    # a = [583563238, 136809000, 54601291, 5797762, 468677897]
    # b = [820642330, 653199778, 785892285, 453599267, 916692569]
    # c = [44577, 90962, 50554, 65697, 87409]

    N, C = 2, 6
    a = [1, 2]
    b = [2, 2]
    c = [4, 4]

    # N, C = 5, 1000000000
    # a = [583563238, 136809000, 54601291, 5797762, 468677897]
    # b = [820642330, 653199778, 785892285, 453599267, 916692569]
    # c = [44577, 90962, 50554, 65697, 87409]

    # N, C = 5, 100000
    # a = [583563238, 136809000, 54601291, 5797762, 468677897]
    # b = [820642330, 653199778, 785892285, 453599267, 916692569]

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
