Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, c, a, b, cost):
    #print(n, c, a, b, cost)
    #print('=====================')
    #print(a)
    #print(b)
    #print(cost)
    #print('=====================')
    #print('=====================

=======
Suggestion 2

def main():
    n,c = map(int,input().split())
    l = []
    for _ in range(n):
        a,b,c = map(int,input().split())
        l.append((a-1,c))
        l.append((b,-c))
    l.sort()
    ans = 0
    fee = 0
    t = 0
    for x,y in l:
        if x != t:
            ans += min(c,fee)*(x-t)
            t = x
        fee += y
    print(ans)
main()

=======
Suggestion 3

def get_input():
    N,C = map(int,input().split())
    v = []
    for i in range(N):
        a,b,c = map(int,input().split())
        v.append((a,b,c))
    return N,C,v

=======
Suggestion 4

def main():
    n,c = map(int, input().split())
    l = []
    for i in range(n):
        a,b,d = map(int, input().split())
        l.append((a,d))
        l.append((b+1,-d))
    l.sort()
    ans = 0
    fee = 0
    t = 0
    for x,y in l:
        if x != t:
            ans += min(c,fee)*(x-t)
            t = x
        fee += y
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(N)]
    abcs.sort()
    #print(abcs)
    #print(N, C)
    #print(abcs)
    #print(abcs[0][0])
    #print(abcs[0][1])
    #print(abcs[0][2])
    #print(abcs[1][0])
    #print(abcs[1][1])
    #print(abcs[1][2])
    #print(abcs[2][0])
    #print(abcs[2][1])
    #print(abcs[2][2])
    #print(abcs[3][0])
    #print(abcs[3][1])
    #print(abcs[3][2])
    #print(abcs[4][0])
    #print(abcs[4][1])
    #print(abcs[4][2])
    #print(abcs[5][0])
    #print(abcs[5][1])
    #print(abcs[5][2])
    #print(abcs[6][0])
    #print(abcs[6][1])
    #print(abcs[6][2])
    #print(abcs[7][0])
    #print(abcs[7][1])
    #print(abcs[7][2])
    #print(abcs[8][0])
    #print(abcs[8][1])
    #print(abcs[8][2])
    #print(abcs[9][0])
    #print(abcs[9][1])
    #print(abcs[9][2])
    #print(abcs[10][0])
    #print(abcs[10][1])
    #print(abcs[10][2])
    #print(abcs[11][0])
    #print(abcs[11][1])
    #print(abcs[11][2])
    #print(abcs[12][0])
    #print(abcs[12][1])
    #print(abcs[12][2])
    #print(abcs[13][0])
    #print(abcs[13][1])
    #print(abcs[13][2])
    #print(abcs[14][0])
    #print(abcs[14][1])
    #print

=======
Suggestion 6

def read_ints():
    return list(map(int, input().split()))

N, C = read_ints()
plans = [read_ints() for _ in range(N)]
plans.sort(key=lambda x:x[0])

=======
Suggestion 7

def solve(n, c, a, b, cost):
    dp = [0] * (10**9 + 1)
    for i in range(n):
        dp[a[i]] += cost[i]
        dp[b[i] + 1] -= cost[i]
    for i in range(10**9):
        dp[i + 1] += dp[i]
    return min(c, min(dp))

=======
Suggestion 8

def main():
    # 读入数据
    N, C = map(int, input().split())
    #print(N, C)
    #print(type(N), type(C))
    #print(type(N) == int, type(C) == int)
    #print(type(N) == float, type(C) == float)
    #print(type(N) == str, type(C) == str)
    #print(type(N) == bool, type(C) == bool)
    #print(type(N) == list, type(C) == list)
    #print(type(N) == tuple, type(C) == tuple)
    #print(type(N) == set, type(C) == set)
    #print(type(N) == dict, type(C) == dict)
    #print(type(N) == complex, type(C) == complex)
    #print(type(N) == object, type(C) == object)
    #print(type(N) == frozenset, type(C) == frozenset)
    #print(type(N) == bytes, type(C) == bytes)
    #print(type(N) == bytearray, type(C) == bytearray)
    #print(type(N) == memoryview, type(C) == memoryview)

    #print(type(N) == str, type(C) == int)
    #print(type(N) == int, type(C) == str)
    #print(type(N) == str, type(C) == float)
    #print(type(N) == float, type(C) == str)
    #print(type(N) == str, type(C) == bool)
    #print(type(N) == bool, type(C) == str)
    #print(type(N) == str, type(C) == list)
    #print(type(N) == list, type(C) == str)
    #print(type(N) == str, type(C) == tuple)
    #print(type(N) == tuple, type(C) == str)
    #print(type(N) == str, type(C) == set)
    #print(type(N) == set, type(C) == str)
    #print(type(N) == str, type(C) == dict)
    #print(type(N) == dict, type(C) == str)
    #print(type(N) == str, type(C) == complex)
    #print(type(N) == complex, type(C) == str)
    #print(type(N) ==

=======
Suggestion 9

def solve():
    # N, C = map(int, input().split())
    N, C = 5, 100000
    # a, b, c = [], [], []
    a = [583563238, 136809000, 54601291, 5797762, 468677897]
    b = [820642330, 653199778, 785892285, 453599267, 916692569]
    c = [44577, 90962, 50554, 65697, 87409]
    # for _ in range(N):
    #     a_i, b_i, c_i = map(int, input().split())
    #     a.append(a_i)
    #     b.append(b_i)
    #     c.append(c_i)
    # print(a, b, c)
    # print(N, C)
    # print(a, b, c)
    # print(a[0], b[0], c[0])
    # print(a[1], b[1], c[1])
    # print(a[2], b[2], c[2])
    # print(a[3], b[3], c[3])
    # print(a[4], b[4], c[4])
    # print(a[5], b[5], c[5])
    # print(a[6], b[6], c[6])
    # print(a[7], b[7], c[7])
    # print(a[8], b[8], c[8])
    # print(a[9], b[9], c[9])
    # print(a[10], b[10], c[10])
    # print(a[11], b[11], c[11])
    # print(a[12], b[12], c[12])
    # print(a[13], b[13], c[13])
    # print(a[14], b[14], c[14])
    # print(a[15], b[15], c[15])
    # print(a[16], b[16], c[16])
    # print(a[17], b[17], c[17])
    # print(a[18], b[18], c[18])
    # print(a[19], b[19], c[19])
    # print(a[20],

=======
Suggestion 10

def solve():
    N,C = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    print(lst)
    print(N,C)
    print(lst[0][0])
    print(lst[0][1])
    print(lst[0][2])
    print(lst[1][0])
    print(lst[1][1])
    print(lst[1][2])
    print(lst[2][0])
    print(lst[2][1])
    print(lst[2][2])
    print(lst[3][0])
    print(lst[3][1])
    print(lst[3][2])
    print(lst[4][0])
    print(lst[4][1])
    print(lst[4][2])
    print(lst[0][0])
    print(lst[0][1])
    print(lst[0][2])
    print(lst[1][0])
    print(lst[1][1])
    print(lst[1][2])
    print(lst[2][0])
    print(lst[2][1])
    print(lst[2][2])
    print(lst[3][0])
    print(lst[3][1])
    print(lst[3][2])
    print(lst[4][0])
    print(lst[4][1])
    print(lst[4][2])
    print(lst[0][0])
    print(lst[0][1])
    print(lst[0][2])
    print(lst[1][0])
    print(lst[1][1])
    print(lst[1][2])
    print(lst[2][0])
    print(lst[2][1])
    print(lst[2][2])
    print(lst[3][0])
    print(lst[3][1])
    print(lst[3][2])
    print(lst[4][0])
    print(lst[4][1])
    print(lst[4][2])
    print(lst[0][0])
    print(lst[0][1])
    print(lst[0][2])
    print(lst[1][0])
    print(lst[1][1])
    print(lst[1][2])
    print(lst[2][0])
    print(lst[2][1])
    print(lst[2][2])
    print(lst[3][0])
    print(lst[3][1])
    print(lst[3][2])
