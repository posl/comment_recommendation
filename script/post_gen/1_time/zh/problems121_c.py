Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ta,tb = map(int,input().split())
        a.append(ta)
        b.append(tb)
    ans = 0
    for i in range(n):
        if m <= b[i]:
            ans += a[i] * m
            break
        else:
            ans += a[i] * b[i]
            m -= b[i]
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
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
Suggestion 3

def get_min_price(n, m, price_list):
    price_list.sort(key=lambda x:x[0])
    total_num = 0
    min_price = 0
    for price in price_list:
        if total_num + price[1] < m:
            total_num += price[1]
            min_price += price[0] * price[1]
        else:
            min_price += price[0] * (m - total_num)
            break
    return min_price

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort()
    ans = 0
    for i in range(n):
        if ab[i][1] >= m:
            ans += ab[i][0] * m
            break
        else:
            ans += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    print(ans)

=======
Suggestion 5

def solve(n, m, a, b):
    # 1. 贪心法
    # 2. 优先队列
    # 3. 二分法

    # 1. 贪心法
    # 1.1 按照单价从小到大排序
    # 1.2 按照单价从小到大购买
    # 1.3 若购买的数量大于m，则停止购买
    # 1.4 若购买的数量小于m，则将剩余的数量乘以单价，加入总金额
    # 1.5 若购买的数量等于m，则返回总金额

    # 2. 优先队列
    # 2.1 将a和b组合为元组，然后按照a从小到大排序，若a相等，则按照b从小到大排序
    # 2.2 将元组放入优先队列
    # 2.3 从优先队列中取出a最小的元组，若b大于m，则将总金额加上m*a，返回总金额
    # 2.4 若b小于m，则将总金额加上b*a，将m减去b，重复2.3
    # 2.5 若b等于m，则将总金额加上b*a，返回总金额

    # 3. 二分法
    # 3.1 按照单价从小到大排序
    # 3.2 二分法查找，从单价最小的开始，直到单价最大的结束
    # 3.3 二分法查找的过程中，每次都计算出购买的数量，若购买的数量大于m，则将右边界减小，若购买的数量小于m，则将左边界增加
    # 3.4 二分法查找的过程中，每次都计算出购买的总金额，若购买

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    #print(n, m)
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        #print(a_i, b_i)
        a.append(a_i)
        b.append(b_i)
    #print(a, b)
    #print(sum(b))
    #print(m)
    if sum(b) <= m:
        print(sum([a[i] * b[i] for i in range(n)]))
    else:
        #print('here')
        total = 0
        for i in range(n):
            if b[i] > m:
                total += a[i] * m
                break
            else:
                total += a[i] * b[i]
                m -= b[i]
        print(total)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A,B))
    C.sort()
    ans = 0
    for a,b in C:
        if b <= M:
            ans += a*b
            M -= b
        else:
            ans += a*M
            M = 0
        if M == 0:
            break
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)

    # print(sum(b))
    if sum(b) <= m:
        print(sum([a[i]*b[i] for i in range(n)]))
    else:
        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))

        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))

        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True

=======
Suggestion 9

def main():
    # N, M = map(int, input().split())
    # AB = [list(map(int, input().split())) for _ in range(N)]
    N = 2
    M = 5
    AB = [[4, 9], [2, 4]]
    # N = 4
    # M = 30
    # AB = [[6, 18], [2, 5], [3, 10], [7, 9]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 4
    # M = 30
    # AB = [[6, 18], [2, 5], [3, 10], [7, 9]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    # N = 1
    # M = 100000
    # AB = [[1000000000, 100000]]
    AB.sort()
    # print(AB)
    ans = 0
    for i in range(N):
        if M > AB[i][1]:
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
    price_1 = []
    price_2 = []
    for i in range(n):
        a,b = map(int,input().split())
        price_1.append(a)
        price_2.append(b)
    price_1 = sorted(price_1)
    price_2 = sorted(price_2)
    sum = 0
    for i in range(m):
        if price_2[0] > price_1[i]:
            sum += price_1[i]
        else:
            sum += price_2[0]
    print(sum)
