Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n, c = map(int, input().split())
    plans = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        plans.append((a, b, c))
    return n, c, plans

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def solve():
    N,C = map(int, input().split())
    a = [0] * N
    b = [0] * N
    c = [0] * N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())
    # print(a,b,c)
    # print(N,C)
    # print(a)
    # print(b)
    # print(c)
    # print()
    # print()
    # print()
    # print()

    # dp[i] 表示第i天的最小花费
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + C
        for j in range(N):
            if i < a[j]:
                dp[i] += c[j]
            elif a[j] <= i <= b[j]:
                dp[i] += min(c[j], dp[a[j]-1] + (i-a[j]+1)*C)
    # print(dp)
    print(dp[N])

=======
Suggestion 4

def main():
    N,C = map(int, input().split())
    #print(N,C)
    array = []
    for i in range(N):
        a,b,c = map(int, input().split())
        array.append([a,b,c])
    #print(array)
    array.sort()
    #print(array)
    result = 0
    for i in range(N):
        start = array[i][0]
        end = array[i][1]
        cost = array[i][2]
        if i == 0:
            result += cost
            prev = end
        else:
            if start == prev:
                result += cost
                prev = end
            else:
                if start - prev > C:
                    result += C
                    result += cost
                    prev = end
                else:
                    result += cost
                    prev = end
    print(result)

=======
Suggestion 5

def main():
    n, c = map(int, input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        d.append(ci)
    #print(a,b,d)
    #print(n,c)
    #print(a[0],b[0],d[0])

    #print(n,c,a,b,d)
    #print(a[0],b[0],d[0])
    #print(a[1],b[1],d[1])
    #print(a[2],b[2],d[2])
    #print(a[3],b[3],d[3])
    #print(a[4],b[4],d[4])

    #print(a[0],b[0],d[0])
    #print(a[1],b[1],d[1])
    #print(a[2],b[2],d[2])
    #print(a[3],b[3],d[3])
    #print(a[4],b[4],d[4])
    #print(a[5],b[5],d[5])
    #print(a[6],b[6],d[6])
    #print(a[7],b[7],d[7])
    #print(a[8],b[8],d[8])
    #print(a[9],b[9],d[9])
    #print(a[10],b[10],d[10])
    #print(a[11],b[11],d[11])
    #print(a[12],b[12],d[12])
    #print(a[13],b[13],d[13])
    #print(a[14],b[14],d[14])
    #print(a[15],b[15],d[15])
    #print(a[16],b[16],d[16])
    #print(a[17],b[17],d[17])
    #print(a[18],b[18],d[18])
    #print(a[19],b[19],d[19])
    #print(a[20],b[20],d[20])
    #print(a[21],b[21

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    #print(N,C)
    #print(type(N),type(C))
    a = []
    b = []
    c = []
    for i in range(N):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    #print(a)
    #print(b)
    #print(c)
    #print(type(a))
    #print(type(b))
    #print(type(c))
    #print(len(a))
    #print(len(b))
    #print(len(c))
    #print(a[0])
    #print(b[0])
    #print(c[0])
    #print(type(a[0]))
    #print(type(b[0]))
    #print(type(c[0]))
    #print(a[1])
    #print(b[1])
    #print(c[1])
    #print(type(a[1]))
    #print(type(b[1]))
    #print(type(c[1]))
    #print(a[2])
    #print(b[2])
    #print(c[2])
    #print(type(a[2]))
    #print(type(b[2]))
    #print(type(c[2]))
    #print(a[3])
    #print(b[3])
    #print(c[3])
    #print(type(a[3]))
    #print(type(b[3]))
    #print(type(c[3]))
    #print(a[4])
    #print(b[4])
    #print(c[4])
    #print(type(a[4]))
    #print(type(b[4]))
    #print(type(c[4]))
    #print(a[5])
    #print(b[5])
    #print(c[5])
    #print(type(a[5]))
    #print(type(b[5]))
    #print(type(c[5]))
    #print(a[6])
    #print(b[6])
    #print(c[6])
    #print(type(a[6]))
    #print(type(b[6]))
    #print(type(c[6]))
    #print(a[7])
    #print(b[7])
    #print(c[7])
    #print(type(a[7]))
    #print(type(b[7]))
    #print(type(c[7]))
    #print(a[8

=======
Suggestion 7

def main():
    N,C = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    C = [AB[i][2] for i in range(N)]
    total = 0
    for i in range(N):
        total += C[i]*(B[i]-A[i])
    print(total)

=======
Suggestion 8

def solve():
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
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)

=======
Suggestion 9

def main():
    n,c = map(int, input().split())
    a = []
    b = []
    cost = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        cost.append(c_i)
    print(n,c)
    print(a)
    print(b)
    print(cost)
    print("end")

=======
Suggestion 10

def get_min_cost(n, c, a, b, cost):
    # 1. get the min cost for each day
    # 2. get the min cost for each day with Snuke Prime
    # 3. get the min cost for each day without Snuke Prime
    # 4. get the min cost for each day
    # 5. get the min cost for the whole period
    min_cost = [0] * n
    min_cost[0] = min(cost[0], c)
    for i in range(1, n):
        min_cost[i] = min_cost[i-1] + min(cost[i], c)
    min_cost_with_prime = [0] * n
    min_cost_with_prime[0] = min_cost[0]
    for i in range(1, n):
        min_cost_with_prime[i] = min_cost_with_prime[i-1] + min(cost[i], c)
        if a[i] - b[i-1] > 1:
            min_cost_with_prime[i] = min(min_cost_with_prime[i], min_cost[i-1] + c)
    min_cost_without_prime = [0] * n
    min_cost_without_prime[0] = cost[0]
    for i in range(1, n):
        min_cost_without_prime[i] = min_cost_without_prime[i-1] + cost[i]
    min_cost_with_prime_2 = [0] * n
    min_cost_with_prime_2[0] = min_cost_without_prime[0]
    for i in range(1, n):
        min_cost_with_prime_2[i] = min_cost_with_prime_2[i-1] + cost[i]
        if a[i] - b[i-1] > 1:
            min_cost_with_prime_2[i] = min(min_cost_with_prime_2[i], min_cost_without_prime[i-1] + c)
    #print(min_cost)
    #print(min_cost_with_prime)
    #print(min_cost_without_prime)
    #print(min_cost_with_prime_2)
    return min(min_cost_with_prime[n-1], min_cost_with_prime_2[n-1])
