Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N, X = map(int, input().split())
    N, X = 10, 1000000000
    # A = [None] * N
    # B = [None] * N
    # for i in range(N):
    #     A[i], B[i] = map(int, input().split())
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    B = [3, 6, 7, 8, 7, 9, 4, 4, 1, 1]
    # print(N, X)
    # print(A)
    # print(B)
    # print()
    # print()
    # print()

    # N, X = 3, 4
    # A = [3, 2, 4]
    # B = [4, 3, 2]

    # N, X = 10, 1000000000
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # B = [3, 6, 7, 8, 7, 9, 4, 4, 1, 1]

    # N, X = 10, 1000000000
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # B = [3, 6, 7, 8, 7, 9, 4, 4, 1, 1]

    # N, X = 10, 1000000000
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # B = [3, 6, 7, 8, 7, 9, 4, 4, 1, 1]

    # N, X = 10, 1000000000
    # A = [3, 1, 4, 1, 5, 9, 2, 6,

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(x)
    #print(n)
    #print(len(a))
    #print(len(b))
    #print(len(a) == len(b))
    #print(len(a) == n)
    #print(len(b) == n)

    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]

    # 二分探索
    def isOK(x):
        # x分でクリアできるステージ数
        cnt = [0] * N
        # あとx分でクリアできるステージ数
        rest = [0] * N
        for i in range(N):
            cnt[i] = max(0, (x - B[i]) // A[i] + 1)
            rest[i] = max(0, (x - B[i]) % A[i])
        cnt.sort()
        # x分でクリアできるステージ数の合計
        total = sum(cnt)
        # あとx分でクリアできるステージ数の合計
        rest_total = sum(rest)
        return total >= X and rest_total <= x

    # 二分探索
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(10 ** 18, 0))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # print(a)
    # print(b)

    # print(a[0] + b[0])
    # print(a[1] + b[1])
    # print(a[0] + b[0] + a[1] + b[1])
    # print(a[0] + b[0] + a[1] + b[1] + a[2] + b[2])

    # print(a[0] + b[0])
    # print(a[1] + b[1])
    # print(a[1] + b[1] + a[0] + b[0])
    # print(a[2] + b[2] + a[1] + b[1] + a[0] + b[0])

    # print(a[0] + b[0])
    # print(a[1] + b[1])
    # print(a[1] + b[1] + a[0] + b[0])
    # print(a[2] + b[2] + a[1] + b[1] + a[0] + b[0])
    # print(a[2] + b[2] + a[1] + b[1] + a[0] + b[0] + a[1] + b[1])

    # print(a[0] + b[0])
    # print(a[1] + b[1])
    # print(a[1] + b[1] + a[0] + b[0])
    # print(a[2] + b[2] + a[1] + b[1] + a[0] + b[0])
    # print(a[2] + b[2] + a[1] + b[1] + a[0] + b[0] + a[1] + b[1])
    # print(a[3] + b[3] + a[2] + b[2] + a[1] + b[1] + a[0] + b[0]

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    # print(N, X)
    # print(AB)
    # print(A)
    # print(B)
    # print()

    # 二分探索
    # ok: X分でクリアできるか
    # ng: X分でクリアできない
    ok = 0
    ng = 10**18
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print(mid)
        # print(f(ok), f(mid), f(ng))
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 6

def solve():
    # 读入数据
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 累计时间
    t = 0
    # 累计通关次数
    ans = 0
    # 遍历阶段
    for a, b in AB:
        # 通关一次
        ans += 1
        # 累计时间
        t += a
        # 如果累计时间超过了限制
        if t > X:
            # 通关次数减去1
            ans -= 1
            # 结束循环
            break
        # 通关一次
        ans += 1
        # 累计时间
        t += b
    # 通关次数减去1
    ans -= 1

    # 输出答案
    print(ans)

solve()

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    # print(N, X, A, B)
    # print(AB)
    # print(A)
    # print(B)
    # print(type(N), type(X), type(A), type(B))
    # print(type(AB))
    # print(type(AB[0]))
    # print(type(AB[0][0]))
    # print(type(AB[0][1]))

    # print(AB[0][0])
    # print(AB[0][1])
    # print(AB[1][0])
    # print(AB[1][1])
    # print(AB[2][0])
    # print(AB[2][1])
    # print(AB[3][0])
    # print(AB[3][1])
    # print(AB[4][0])
    # print(AB[4][1])
    # print(AB[5][0])
    # print(AB[5][1])
    # print(AB[6][0])
    # print(AB[6][1])
    # print(AB[7][0])
    # print(AB[7][1])
    # print(AB[8][0])
    # print(AB[8][1])
    # print(AB[9][0])
    # print(AB[9][1])

    # print(X, X+1, X+2, X+3, X+4, X+5, X+6, X+7, X+8, X+9)
    # print(X, X+1, X+2, X+3, X+4, X+5, X+6, X+7, X+8, X+9)
    # print(A[0], A[1], A[2], A[3], A[4], A[5], A[6], A[7], A[8], A[9])
    # print(A[0], A[1], A[2], A[3], A[4], A[5], A[6], A[

=======
Suggestion 8

def main():
    n,x=map(int,input().split())
    ab=[]
    for i in range(n):
        ab.append(list(map(int,input().split())))
    a,b=zip(*ab)
    a=list(a)
    b=list(b)
    #print(a)
    #print(b)
    time=[]
    for i in range(n):
        time.append(a[i]+b[i])
    #print(time)
    #print(sum(time))
    #print(x)
    #print(sum(time)/x)
    if sum(time)<=x:
        print(n)
    else:
        time.sort()
        #print(time)
        #print(sum(time))
        #print(x)
        count=0
        for i in time:
            if x>=i:
                count+=1
                x-=i
            else:
                break
        print(count)
main()

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #print(AB)
    #N,X = 3,4
    #AB = [[3,4],[2,3],[4,2]]
    #N,X = 10,1000000000
    #AB = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #print(AB)
    #N,X = 3,4
    #AB = [[3,4],[2,3],[4,2]]
    #print(AB)
    #N,X = 10,1000000000
    #AB = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #print(AB)
    #N,X = 10,1000000000
    #AB = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #print(AB)
    #N,X = 3,4
    #AB = [[3,4],[2,3],[4,2]]
    #print(AB)
    #N,X = 10,1000000000
    #AB = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #print(AB)
    #N,X = 3,4
    #AB = [[3,4],[2,3],[4,2]]
    #print(AB)
    #N,X = 10,1000000000
    #AB = [[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #print(AB)
    #N,X = 3,4
    #AB = [[

=======
Suggestion 10

def solve(n,x,ab):
    a = [ab[i][0] for i in range(n)]
    b = [ab[i][1] for i in range(n)]
    #print(a)
    #print(b)
    min_time = min(a)
    #print(min_time)
    min_index = a.index(min_time)
    #print(min_index)
    if x == 1:
        return min_time + b[min_index]
    else:
        if x % 2 == 0:
            return min_time * x + b[min_index]
        else:
            return min_time * x + min_time + b[min_index]

n,x = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
print(solve(n,x,ab))
