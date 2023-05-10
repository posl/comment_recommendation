Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    #print(N, C)
    #print(type(N), type(C))
    #print(N, C)
    #print

=======
Suggestion 2

def main():
    n, c = map(int, input().split())
    #print(n, c)
    abcs = []
    for i in range(n):
        abcs.append(list(map(int, input().split())))
    #print(abcs)
    abcs.sort()
    #print(abcs)
    #print('------')
    #print(n, c)
    #print(abcs)
    #print('-----

=======
Suggestion 3

def calc_cost(services, c):
    cost = 0
    for service in services:
        cost += service[2]
    cost += c
    return cost

=======
Suggestion 4

def solve():
    N, C = map(int, input().split())
    #print(N, C)
    abc = []
    for i in range(N):
        a, b, c = map(int, input().split())
        #print(a, b, c)
        abc.append((a, b, c))
    #print(abc)

    # 1日ごとに支払う金額を計算する
    day = [0] * (10 ** 9 + 2)
    for a, b, c in abc:
        day[a] += c
        day[b + 1] -= c
    #print(day)

    # 累積和を計算する
    for i in range(1, len(day)):
        day[i] += day[i - 1]
    #print(day)

    # すぬけプライムに加入する日を探す
    prime = [0] * (10 ** 9 + 2)
    for i in range(1, len(day)):
        if day[i] > C:
            prime[i] = 1
    #print(prime)

    # 累積和を計算する
    for i in range(1, len(prime)):
        prime[i] += prime[i - 1]
    #print(prime)

    # 各サービスを利用する日を探す
    ans = 0
    for a, b, c in abc:
        if prime[b] - prime[a - 1] == 0:
            ans += c
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    events = []
    for i in range(N):
        a, b, c = map(int, input().split())
        events.append([a-1, c])
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
Suggestion 6

def solve():
    N,C = map(int,input().split())
    events = []
    for i in range(N):
        a,b,c = map(int,input().split())
        events.append((a-1,c))
        events.append((b,-c))
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x,y in events:
        if x != t:
            ans += min(C,fee) * (x-t)
            t = x
        fee += y
    print(ans)

=======
Suggestion 7

def main():
    n, c = map(int, input().split())
    l = []
    for i in range(n):
        a, b, d = map(int, input().split())
        l.append([a, d])
        l.append([b+1, -d])
    l.sort()
    s = 0
    ans = 0
    t = 0
    for i in range(len(l)):
        if l[i][0] != t:
            ans += min(c, s) * (l[i][0] - t)
            t = l[i][0]
        s += l[i][1]
    print(ans)

=======
Suggestion 8

def get_input_data():
    n,c = map(int,input().split())
    service = []
    for i in range(n):
        a,b,c = map(int,input().split())
        service.append([a,b,c])
    return n,c,service

=======
Suggestion 9

def main():
    n, c = map(int, input().split())
    #print(n, c)
    #a = []
    #b = []
    #c = []
    #for i in range(n):
    #    a[i], b[i], c[i] = map(int, input().split())
    #    print(a[i], b[i], c[i])
    #print(a)
    #print(b)
    #print(c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    #for i in range(n):
    #    a, b, c = map(int, input().split())
    #    print(a, b, c)
    #print(n, c)
    a = []
    b = []
    c = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    #print(a)
    #print(b)
    #print(c)
    #print(n

=======
Suggestion 10

def solve():
    N,C = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    #各日の支払い金額を計算する
    #日付ごとに、何日間すぬけプライムを利用するかを調べる
    #各日の支払い金額を計算する
    #各日の支払い金額を合計する
    #最小の支払い金額を出力する
    #各日の支払い金額を計算する
    #日付ごとに、何日間すぬけプライムを利用するかを調べる
    #各日の支払い金額を計算する
    #各日の支払い金額を合計する
    #最小の支払い金額を出力する
    #各日の支払い金額を計算する
    #日付ごとに、何日間すぬけプライムを利用するかを調べる
    #各日の支払い金額を計算する
    #各日の支払い金額を合計する
    #最小の支払い金額を出力する
    #各日の支払い金額を計算する
    #日付ごとに、何日間すぬけプライムを利用するかを調べる
    #各日の支払い金額を計算する
    #各日の支払い金額を合計する
    #最小の支払い金額を出力する
    #各日の支払い金額を計算する
    #日付ごとに、何日間すぬけプラ
