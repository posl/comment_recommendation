Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    in_str = input()
    in_list = in_str.split()
    n = int(in_list[0])
    c = int(in_list[1])
    service_list = []
    for i in range(n):
        service_str = input()
        service_list.append(service_str.split())
    return n, c, service_list

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    d = []
    for i in range(N):
        a, b, c = map(int, input().split())
        d.append((a, c))
        d.append((b+1, -c))
    d.sort()
    ans = 0
    fee = 0
    t = 0
    for i in range(len(d)):
        if d[i][0] != t:
            ans += min(C, fee) * (d[i][0] - t)
            t = d[i][0]
        fee += d[i][1]
    print(ans)

=======
Suggestion 3

def get_min_cost(n, c, l):
    min_cost = 0
    for i in range(n):
        min_cost += l[i][2]
    return min_cost

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    # print(ABC)

    # dp = [0] * (10**9 + 1)
    dp = [0] * (10**9 + 1)
    dp[0] = 0

    for i in range(1, ABC[-1][1] + 1):
        dp[i] = dp[i-1] + C
        for j in range(N):
            if i >= ABC[j][0]:
                dp[i] = min(dp[i], dp[ABC[j][0]] + ABC[j][2] + (i - ABC[j][0]) * ABC[j][1])

    print(dp[ABC[-1][1]])

=======
Suggestion 6

def solve():
    n, c = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]

    # 1. 每天都订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    print(ans)

    # 2. 从第 2 天开始订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    print(ans)

    # 3. 从第 2 天开始订阅，并且在第 1 天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if a == 1)
    print(ans)

    # 4. 从第 2 天开始订阅，并且在最后一天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if b == 10 ** 9)
    print(ans)

    # 5. 从第 2 天开始订阅，并且在第 1 天和最后一天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if a == 1)
    ans += min(c for

=======
Suggestion 7

def main():
    s = input().split()
    N = int(s[0])
    C = int(s[1])
    a = []
    b = []
    c = []
    for i in range(N):
        s = input().split()
        a.append(int(s[0]))
        b.append(int(s[1]))
        c.append(int(s[2]))
    d = []
    for i in range(N):
        d.append((a[i],c[i]))
        d.append((b[i]+1,-c[i]))
    d.sort(key=lambda x:x[0])
    ans = 0
    t = 0
    x = 0
    for i in range(2*N):
        if d[i][0] != x:
            ans += min(C,t)*(d[i][0]-x)
            x = d[i][0]
        t += d[i][1]
    print(ans)

=======
Suggestion 8

def main():
    n,c = map(int, input().split())
    #print(n,c)
    a = []
    b = []
    d = []
    for i in range(n):
        ai,bi,di = map(int, input().split())
        a.append(ai)
        b.append(bi)
        d.append(di)
    #print(a,b,d)
    #print("n=",n)
    #print("c=",c)
    #print("a=",a)
    #print("b=",b)
    #print("d=",d)
    #print("sum(d)=",sum(d))
    #print("sum(b)=",sum(b))
    #print("sum(a)=",sum(a))
    #print("sum(d) + c * (sum(b) - sum(a))=",sum(d) + c * (sum(b) - sum(a)))
    #print("c * (sum(b) - sum(a))=",c * (sum(b) - sum(a)))
    #print("sum(d) + c * (sum(b) - sum(a))=",sum(d) + c * (sum(b) - sum(a)))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) + sum(d))
    #print("c * (sum(b) - sum(a)) + sum(d)=",c * (sum(b) - sum(a)) +

=======
Suggestion 9

def main():
    n, c = map(int, input().split())
    a = []
    b = []
    cost = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        cost.append(c_i)
    #print(a)
    #print(b)
    #print(cost)
    min_cost = 0
    for i in range(n):
        min_cost += cost[i] * (b[i] - a[i] + 1)
    #print(min_cost)
    #print(c)
    #print(a)
    #print(b)
    min_cost += c
    #print(min_cost)
    #print(a)
    #print(b)
    #print(cost)
    for i in range(n - 1):
        if b[i] + 1 == a[i + 1]:
            min_cost -= cost[i] + cost[i + 1]
            if cost[i] > cost[i + 1]:
                min_cost -= cost[i + 1] * (b[i + 1] - a[i + 1] + 1)
                min_cost += cost[i] * (b[i + 1] - a[i + 1] + 1)
            #print(min_cost)
    print(min_cost)

=======
Suggestion 10

def main():
    N, C = map(int, input().split())
    service = []
    for i in range(N):
        service.append(list(map(int, input().split())))

    #print(N, C)
    #print(service)

    #service = [[1, 2, 4], [2, 2, 4]]
    #service = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]

    #service = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #N = 5
    #C = 1000000000
    #service = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]

    #service = [[1, 2, 4], [2, 2, 4]]
    #N = 2
    #C = 6

    #service = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    #N = 3
    #C = 3

    #service = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    #N = 3
    #C = 10

    #service = [[1, 1000000000, 1000000000], [1000000000, 1000000000, 1000000000]]
    #N = 2
    #C = 1000000000

    #service = [[1, 100000
