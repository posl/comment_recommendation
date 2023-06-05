Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    minP = 1000000000
    for i in range(N):
        if X[i] > 0:
            if P[i] < minP:
                minP = P[i]
    if minP == 1000000000:
        print(-1)
    else:
        print(minP)

=======
Suggestion 2

def solve():
    N = int(input())
    A_P_X = []
    for i in range(N):
        A_P_X.append(list(map(int, input().split())))
    A_P_X.sort(key=lambda x: x[0])
    min_price = float('inf')
    for i in range(N):
        if A_P_X[i][2] > 0:
            min_price = min(min_price, A_P_X[i][1])
    if min_price == float('inf'):
        print(-1)
    else:
        print(min_price)
solve()

=======
Suggestion 3

def buy_play_snuke(n, shop_list):
    min_cost = -1
    for shop in shop_list:
        shop_cost = shop[1]
        shop_stock = shop[2]
        shop_walk_time = shop[0]
        if shop_stock > 0:
            if min_cost == -1:
                min_cost = shop_cost
            else:
                if shop_cost < min_cost:
                    min_cost = shop_cost
    return min_cost

=======
Suggestion 4

def main():
    num = int(input())
    a = []
    p = []
    x = []
    for i in range(num):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min = 10**9
    for i in range(num):
        if x[i] > 0:
            if p[i] < min:
                min = p[i]
    if min == 10**9:
        print(-1)
    else:
        print(min)

=======
Suggestion 5

def get_min_price(n, shops):
    min_price = -1
    for i in range(n):
        if shops[i][2] > 0:
            if min_price == -1:
                min_price = shops[i][1]
            else:
                min_price = min(min_price, shops[i][1])
    return min_price

=======
Suggestion 6

def buy_play_snuke(N, shop_list):
    min_price = -1
    for shop in shop_list:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            elif min_price > shop[1]:
                min_price = shop[1]
    return min_price

=======
Suggestion 7

def main():
    n = int(input())

    # 读取数据
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)

    # 判断是否能购买
    flag = False
    for i in range(n):
        if x[i] > 0:
            flag = True
            break
    if flag == False:
        print(-1)
        return

    # 计算最低资金量
    min_price = 10**9
    for i in range(n):
        if x[i] > 0 and p[i] < min_price:
            min_price = p[i]
    print(min_price)

=======
Suggestion 8

def main():
    # 读取输入
    n = int(input())
    stores = []
    for i in range(n):
        store = list(map(int, input().split()))
        stores.append(store)
    # print(stores)

    # 计算结果
    result = -1
    for i in range(n):
        if stores[i][2] > 0:
            if result == -1:
                result = stores[i][1]
            elif result > stores[i][1]:
                result = stores[i][1]

    # 输出结果
    print(result)

=======
Suggestion 9

def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)

    min_cost = 0
    for i in range(N):
        if X[i] > 0:
            if min_cost == 0:
                min_cost = P[i]
            else:
                min_cost = min(min_cost, P[i])
    if min_cost == 0:
        print(-1)
        return

    print(min_cost)

=======
Suggestion 10

def getMinMoney(N, A, P, X):
    minMoney = -1
    for i in range(N):
        if X[i] > 0:
            money = P[i]
            if minMoney == -1:
                minMoney = money
            else:
                minMoney = min(minMoney, money)
    return minMoney

N = int(input())
A = []
P = []
X = []
for i in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

minMoney = getMinMoney(N, A, P, X)

print(minMoney)
