Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 二分法
    def is_ok(x):
        # x円でM本以上買えるか？
        # x円で買える本数を計算
        num = 0
        for i in range(N):
            if A[i] > x:
                continue
            num += (x - A[i]) // B[i] + 1
        return num >= M

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10 ** 18 + 1))


main()

=======
Suggestion 2

def solve(n, m, a, b):
    # 二分查找
    # 二分查找的上下限分别是0和10^9+1
    left = 0
    right = 10**9 + 1
    while left + 1 < right:
        mid = (left + right) // 2
        # 验证mid是否满足条件
        # 用mid元能买到的饮料数
        num = 0
        for i in range(n):
            # 用mid元能买到的饮料数
            if a[i] >= mid:
                num += b[i]
        if num >= m:
            # mid元能买到的饮料数大于等于m，说明mid元太大了，下次查找时mid应该小一些
            right = mid
        else:
            # mid元能买到的饮料数小于m，说明mid元太小了，下次查找时mid应该大一些
            left = mid
    return left

=======
Suggestion 3

def main():
    N, M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += M * AB[i][0]
            break
        else:
            ans += AB[i][1] * AB[i][0]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 4

def solve(n,m,ab):
    # 二分法
    # ab.sort(key=lambda x:x[0]/x[1],reverse=True)
    # print(ab)
    # sum = 0
    # for i in range(n):
    #     if m == 0:
    #         break
    #     if m < ab[i][1]:
    #         sum += ab[i][0] / ab[i][1] * m
    #         m = 0
    #     else:
    #         sum += ab[i][0]
    #         m -= ab[i][1]
    # return sum

    # 贪心
    ab.sort(key=lambda x:x[0],reverse=True)
    sum = 0
    for i in range(n):
        if m == 0:
            break
        if m < ab[i][1]:
            sum += ab[i][0] * m
            m = 0
        else:
            sum += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    return sum

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    num = 0
    sum = 0
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    while num < m:
        min = 1000000001
        for i in range(n):
            if min > a[i]:
                min = a[i]
                j = i
        if num + b[j] < m:
            sum += a[j] * b[j]
            num += b[j]
            a[j] = 1000000001
        else:
            sum += a[j] * (m - num)
            num = m
    print(sum)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    min = 0
    sum = 0
    for i in range(n):
        min += a[i] * b[i]
        sum += b[i]
    if sum == m:
        print(min)
    elif sum > m:
        for i in range(n):
            if b[i] > m:
                min -= a[i] * b[i]
                min += a[i] * m
                print(min)
                break
            elif b[i] == m:
                min -= a[i] * b[i]
                min += a[i] * m
                print(min)
                break
            else:
                min -= a[i] * b[i]
                m -= b[i]
    else:
        print(min)

=======
Suggestion 7

def shop_list():
    #初始化
    n = 0
    m = 0
    shop_list = []
    #输入
    n, m = map(int, input().split())
    for i in range(n):
        shop_list.append(list(map(int, input().split())))
    #排序
    shop_list.sort(key=lambda x: x[0])
    #计算
    count = 0
    money = 0
    for i in range(n):
        if count + shop_list[i][1] < m:
            count += shop_list[i][1]
            money += shop_list[i][0] * shop_list[i][1]
        else:
            money += shop_list[i][0] * (m - count)
            break
    #输出
    print(money)
shop_list()

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(a.index(min(a)))
    #print(b[a.index(min(a))])
    #print(min(a))
    #print(b[a.index(min(a))])
    if m <= b[a.index(min(a))]:
        print(min(a) * m)
    else:
        print(min(a) * b[a.index(min(a))] + min(a) * (m - b[a.index(min(a))]))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    shop = []
    for i in range(n):
        a,b = map(int,input().split())
        shop.append([a,b])
    shop.sort()
    sum = 0
    for s in shop:
        if m <= s[1]:
            sum += m * s[0]
            break
        else:
            sum += s[1] * s[0]
            m -= s[1]
    print(sum)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    s = 0
    for i in range(n):
        s += b[i]
    if s <= m:
        print(sum(a))
    else:
        c = []
        for i in range(n):
            c.append(a[i]/b[i])
        c.sort()
        s = 0
        for i in range(n):
            s += b[i]
            if s >= m:
                break
        print(sum(c[:i+1])*m)
