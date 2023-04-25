Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))
    AB.sort()
    t = 0
    ans = 0
    for ab in AB:
        ans += min(C, t) * (ab[0] - t)
        t = ab[0]
        t += ab[1]
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append([a, c])
        A.append([b+1, -c])
    A.sort()
    ans = 0
    sum = 0
    prev = 0
    for a in A:
        ans += min(C, sum) * (a[0] - prev)
        sum += a[1]
        prev = a[0]
    print(ans)

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))
    AB.sort()
    ans = 0
    d = 0
    t = 0
    for a, b in AB:
        ans += min(C, d) * (a - t)
        d += b
        t = a
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    abcs = [tuple(map(int, input().split())) for _ in range(N)]
    abcs.sort(key=lambda x: x[1])
    dp = [0] * (abcs[-1][1] + 1)
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1]
        for j in range(N):
            if abcs[j][1] == i:
                dp[i] = min(dp[i], dp[abcs[j][0] - 1] + abcs[j][2])
    print(min(dp[-1], C * abcs[-1][1]))

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort()

    ans = 0
    for i in range(N):
        ans += ABC[i][2] * (ABC[i][1] - ABC[i][0] + 1)
    ans += C * (ABC[-1][1] - ABC[0][0] + 1)

    for i in range(N - 1):
        ans -= ABC[i][2] * (ABC[i + 1][0] - ABC[i][1] - 1)
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, i

=======
Suggestion 7

def main():
    n, c = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(n)]
    abcs.sort()
    ans = 0
    t = 0
    for abc in abcs:
        a, b, c = abc
        t += (a - t) * c
        ans += (b - a + 1) * c
    print(ans + (c - t))

=======
Suggestion 8

def main():
    #N: number of services
    #C: price of Snuke Prime
    #a_i: start date of the i-th service
    #b_i: end date of the i-th service
    #c_i: price of the i-th service
    N, C = map(int, input().split())
    #service_list: list of lists
    #service_list[i] = [a_i, b_i, c_i]
    service_list = []
    for i in range(N):
        a_i, b_i, c_i = map(int, input().split())
        service_list.append([a_i, b_i, c_i])
    #sort service_list by a_i
    service_list.sort()
    #print(service_list)
    #service_list2: list of lists
    #service_list2[i] = [a_i, b_i, c_i, c_i_sum]
    #c_i_sum: sum of c_i from a_i to b_i
    service_list2 = []
    for i in range(N):
        a_i = service_list[i][0]
        b_i = service_list[i][1]
        c_i = service_list[i][2]
        c_i_sum = c_i
        for j in range(i+1, N):
            if service_list[j][0] == a_i:
                c_i_sum += service_list[j][2]
            else:
                break
        service_list2.append([a_i, b_i, c_i, c_i_sum])
    #print(service_list2)
    #service_list3: list of lists
    #service_list3[i] = [a_i, b_i, c_i, c_i_sum, c_i_sum_prime]
    #c_i_sum_prime: sum of c_i from a_i to b_i with Snuke Prime
    service_list3 = []
    for i in range(N):
        a_i = service_list2[i][0]
        b_i = service_list2[i][1]
        c_i = service_list2[i][2]
        c_i_sum = service_list2[i][3]
        c_i_sum_prime = c_i_sum
        for j in range(i+1, N):
            if service_list2[j][0] == a_i:
                if service_list2[j][1] < b_i:
                    c_i_sum_prime += service_list2

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    # a_i, b_i, c_i
    service = [list(map(int, input().split())) for _ in range(N)]
    service.sort(key=lambda x: x[1])
    #print(service)
    # 1-indexed
    dp = [0] * (10**9+1)
    for i in range(N):
        a, b, c = service[i]
        dp[a] += c
        dp[b+1] -= c
    for i in range(1, 10**9+1):
        dp[i] += dp[i-1]
    ans = min([x * C for x in dp])
    print(ans)
