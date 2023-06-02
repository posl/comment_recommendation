Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append([a, b])
    data = sorted(data, key=lambda x: x[0])
    ans = 0
    cnt = 0
    for i in range(n):
        if cnt + data[i][1] >= m:
            ans += data[i][0] * (m - cnt)
            break
        else:
            ans += data[i][0] * data[i][1]
            cnt += data[i][1]
    print(ans)

=======
Suggestion 2

def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照价格升序排序
    ab.sort()
    # 贪心算法
    ans = 0
    for a, b in ab:
        if m <= b:
            ans += a * m
            break
        else:
            ans += a * b
            m -= b
    # 输出结果
    print(ans)

=======
Suggestion 3

def solve(n,m,ab):
    ab.sort(key=lambda x:x[0])
    count=0
    sum=0
    for i in range(n):
        if count+ab[i][1]<=m:
            count+=ab[i][1]
            sum+=ab[i][0]*ab[i][1]
        else:
            sum+=ab[i][0]*(m-count)
            return sum
    return sum

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[0])
    #print(a_b)
    count = 0
    money = 0
    for i in range(n):
        if count >= m:
            break
        if count + a_b[i][1] <= m:
            count += a_b[i][1]
            money += a_b[i][0] * a_b[i][1]
        else:
            money += (m - count) * a_b[i][0]
            count += (m - count)
    print(money)

=======
Suggestion 5

def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照a从小到大排序
    ab.sort()
    # 从最小的开始买，直到买够m罐
    ans = 0
    for a, b in ab:
        if b < m:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum = sum + a*b
    print(sum//m)

=======
Suggestion 7

def solve(n, m, a, b):
    # 二分查找
    # 二分查找的上下界
    lower = 0
    upper = 10 ** 18 + 1
    # 二分查找的循环
    while lower + 1 < upper:
        # 中间值
        mid = (lower + upper) // 2
        # 可以买到的数量
        num = 0
        # 用mid日元可以买到的数量
        for i in range(n):
            num += min(a[i], mid // b[i])
        # 判断可以买到的数量是否大于等于m
        if num >= m:
            upper = mid
        else:
            lower = mid
    return upper

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    price = []
    for i in range(n):
        a,b = map(int,input().split())
        price.append([a,b])
    price.sort()
    #print(price)
    total = 0
    for i in range(n):
        if m >= price[i][1]:
            total += price[i][0] * price[i][1]
            m -= price[i][1]
        else:
            total += price[i][0] * m
            m = 0
    print(total)

=======
Suggestion 9

def calculate():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(M)

    #print(type(N))
    #print(type(M))
    #print(type(A))
    #print(type(B))

    #print(len(A))
    #print(len(B))

    #print(type(A[0]))
    #print(type(B[0]))

    #print(sum(B))

    if sum(B) < M:
        print("输入有误")
        return

    #print("输入正确")

    #print("开始计算")

    #print("先计算最便宜的，然后再计算最贵的")
    #print("A中最便宜的")
    #print(min(A))
    #print("B中最便宜的")
    #print(min(B))

    #print("A中最贵的")
    #print(max(A))
    #print("B中最贵的")
    #print(max(B))

    #print("A中最便宜的")
    #print(min(A))
    #print("B中最贵的")
    #print(max(B))

    #print("A中最贵的")
    #print(max(A))
    #print("B中最便宜的")
    #print(min(B))

    #print("A中最便宜的")
    #print(min(A))
    #print("B中最便宜的")
    #print(min(B))

    #print("A中最贵的")
    #print(max(A))
    #print("B中最贵的")
    #print(max(B))

    #print("A中最便宜的")
    #print(min(A))
    #print("B中最贵的")
    #print(max(B))

    #print("A中最贵的")
    #print(max(A))
    #print("B中最便宜的")
    #print(min(B))

    #print("A中最便宜的")
    #print(min(A))
    #print("B中最便宜

=======
Suggestion 10

def read_int():
    return int(input())
