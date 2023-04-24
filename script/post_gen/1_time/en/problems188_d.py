Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append([a, c])
        AB.append([b+1, -c])
    AB.sort(key=lambda x: x[0])
    ans = 0
    cost = 0
    t = 0
    for ab in AB:
        ans += min(C, cost)*(ab[0]-t)
        cost += ab[1]
        t = ab[0]
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))

    AB.sort()
    ans = 0
    prev = 0
    total = 0
    for i in range(len(AB)):
        if i > 0:
            ans += min(total, C) * (AB[i][0] - prev)
        prev = AB[i][0]
        total += AB[i][1]

    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    A = [0] * N
    B = [0] * N
    C = [0] * N
    for i in range(N):
        A[i], B[i], C[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)
    #print(B)
    #print(C)
    #print(A)
    #print(B)
    #print(C)
    #print(N, C)
    #print(A)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    abcs = []
    for _ in range(N):
        abcs.append(list(map(int, input().split())))
    abcs.sort(key=lambda x: x[0])
    days = [0] * (10**9 + 1)
    for abc in abcs:
        a, b, c = abc
        days[a] += c
        days[b + 1] -= c
    for i in range(1, len(days)):
        days[i] += days[i - 1]
    days = list(map(lambda x: min(x, C), days))
    for i in range(1, len(days)):
        days[i] += days[i - 1]
    print(days[-1])

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(N)]
    abcs.sort(key=lambda x: x[1])
    ans = 0
    for a, b, c in abcs:
        ans += (b - a + 1) * c
    for i in range(N):
        # 1つのサービスを選ぶ
        # そのサービスの開始日より前に開始するサービスがあれば、
        # そのサービスの開始日までにサブスクを購入する
        # そのサービスの終了日より後に終了するサービスがあれば、
        # そのサービスの終了日までにサブスクを購入する
        # サブスクを購入するときは、その日に使うサービスの料金を引く
        # 1つのサービスにつき、最大で2回サブスクを購入する
        # サブスクを購入する日には、その日に使うサービスの料金を引く
        # 1つのサービスにつき、最大で2回サブスクを購入する
        # サブスクを購入する日には、その日に使うサービスの料金を引く
        # 1つのサービスにつき、最大で2回サブスクを購入する
        # サブスクを購入する日には、その日に使うサービスの料金を引く
        # 1つのサービスにつき、最大で2回サブスクを購入する
        # サブスクを購入する日には、その日に使うサービスの料金を引く
        # 1つのサービスにつき、

=======
Suggestion 6

def main():
    n, c = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(n)]
    abcs.sort(key=lambda x: x[0])
    abcs.sort(key=lambda x: x[1])
    dp = [0] * (abcs[-1][1] + 1)
    for i in range(n):
        a, b, c = abcs[i]
        dp[b] = max(dp[b], dp[a - 1] + c)
    for i in range(1, len(dp)):
        dp[i] = max(dp[i], dp[i - 1])
    print(sum([c for a, b, c in abcs]) - min(dp))

=======
Suggestion 7

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) + [i] for i in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([10**9, 10**9, 10**9])
    ans = 0
    cnt = 0
    prev = 0
    for i in range(N):
        if prev == AB[i][0]:
            cnt += 1
        else:
            cnt = 0
        ans += min(C, AB[i][1] - AB[i][0] + 1) * AB[i][2]
        prev = AB[i][0]
    print(ans)

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    AB.append([10**9+1, 0])
    ans = 0
    for i in range(N):
        ans += (AB[i+1][0] - AB[i][0]) * min(C, AB[i][1])
    print(ans)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    #各サービスの開始日と終了日をリストに格納
    start = []
    end = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        start.append(a)
        end.append(b)
    #開始日と終了日をソート
    start.sort()
    end.sort()
    #各サービスの開始日と終了日をインデックスにして、開始日の数をカウント
    #終了日の数を引くことで、開始日と終了日の積集合をカウント
    start_count = [0] * (10 ** 9 + 1)
    end_count = [0] * (10 ** 9 + 1)
    for i in range(N):
        start_count[start[i]] += 1
        end_count[end[i]] += 1
    #開始日と終了日のカウントを累積和
    sc = [0]
    ec = [0]
    for i in range(10 ** 9 + 1):
        sc.append(sc[i] + start_count[i])
        ec.append(ec[i] + end_count[i])
    #開始日と終了日の積集合をカウント
    #開始日と終了日の積集合が0の場合、サービスは一つも使っていない
    #開始日と終了日の積集合が1以上の場合、サービスを使っている
    #開始日と終了日の積集合が2以上の場合、サービスを使っている
    #開始日と終了日の積集合が3以上の場合、サービスを使っている
    #開始日と終了日の積集合が4以上の場合、サービスを使っている
    #開始日と終了日の積集合が5以上

=======
Suggestion 10

def main():
    #入力
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for i in range(N)]

    #日付と利用料金のリストを作成
    date_price = list()
    for i in range(N):
        date_price.append([abc[i][0], abc[i][2]])
        date_price.append([abc[i][1]+1, -abc[i][2]])

    #日付と利用料金のリストを日付でソート
    date_price.sort()

    #日付と利用料金のリストを使って計算
    date = date_price[0][0]
    price = date_price[0][1]
    total_price = date_price[0][1]
    for i in range(1, 2*N):
        if date_price[i][0] == date:
            price += date_price[i][1]
            total_price += date_price[i][1]
        else:
            date = date_price[i][0]
            price += date_price[i][1]
            if price < C:
                total_price += price
            else:
                total_price += C

    #出力
    print(total_price)
