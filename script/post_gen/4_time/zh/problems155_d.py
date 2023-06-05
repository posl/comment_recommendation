Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(a, b):
    return a*b

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    a.reverse()
    a.append(0)
    a.reverse()
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) // 2
        s = 0
        for i in range(n):
            if a[i] > 0:
                break
            if a[i] * a[i] <= a[m]:
                s += n - i - 1
            else:
                j = n - 1
                while a[i] * a[j] > a[m] and j > i:
                    j -= 1
                s += n - j - 1
        if s < k:
            l = m
        else:
            r = m
    print(a[r])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # print(n, k)
    # print(a)

    # 二分探索
    def is_ok(x):
        # x以上のペアの数がk以上かどうか
        cnt = 0
        for i in range(n):
            if a[i] >= 0:
                # a[i]以上のペアの数
                l = i
                r = n
                while r-l>1:
                    m = (l+r)//2
                    if a[i] * a[m] <= x:
                        l = m
                    else:
                        r = m
                cnt += n - l - 1
            else:
                # a[i]以下のペアの数
                l = -1
                r = i
                while r-l>1:
                    m = (l+r)//2
                    if a[i] * a[m] <= x:
                        r = m
                    else:
                        l = m
                cnt += l + 1
        # print(x, cnt)
        return cnt >= k

    # 二分探索
    # 求める値はx
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    # print(is_ok(6))
    # print(is_ok(7))
    # print(is_ok(8))
    # print(is_ok(9))
    # print(is_ok(10))
    # print(is_ok(11))
    # print(is_ok(12))
    # print(is_ok(13))
    # print(is_ok(14))
    # print(is_ok(15))
    # print(is_ok(16))
    # print(is_ok(17))
    # print(is_ok(18))
    # print(is_ok(19))
    # print(is_ok(20))
    # print(is_ok(21))
    # print(is_ok(22))
    # print(is_ok(23))
    # print(is_ok(24))
    # print(is_ok(25))
    # print(is

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    max = 10**9
    min = -10**9
    while max - min > 1:
        x = (max + min) // 2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while r - l > 1:
                    c = (l + r) // 2
                    if A[c] * A[i] < x:
                        r = c
                    else:
                        l = c
                count += N - r
            else:
                l = -1
                r = N
                while r - l > 1:
                    c = (l + r) // 2
                    if A[c] * A[i] < x:
                        l = c
                    else:
                        r = c
                count += r
            if A[i] * A[i] < x:
                count -= 1
        count //= 2
        if count < K:
            min = x
        else:
            max = x
    print(max)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    # print(len(A))
    # print(((N * (N - 1)) / 2))
    # print(K)

    if K <= ((N * (N - 1)) / 2):
        # print("0")
        # print(A[0])
        # print(A[1])
        # print(A[2])
        # print(A[3])
        # print(A[4])
        # print(A[5])
        # print(A[6])
        # print(A[7])
        # print(A[8])
        # print(A[9])
        # print(A[10])
        # print(A[11])
        # print(A[12])
        # print(A[13])
        # print(A[14])
        # print(A[15])
        # print(A[16])
        # print(A[17])
        # print(A[18])
        # print(A[19])
        # print(A[20])
        # print(A[21])
        # print(A[22])
        # print(A[23])
        # print(A[24])
        # print(A[25])
        # print(A[26])
        # print(A[27])
        # print(A[28])
        # print(A[29])
        # print(A[30])
        # print(A[31])
        # print(A[32])
        # print(A[33])
        # print(A[34])
        # print(A[35])
        # print(A[36])
        # print(A[37])
        # print(A[38])
        # print(A[39])
        # print(A[40])
        # print(A[41])
        # print(A[42])
        # print(A[43])
        # print(A[44])
        # print(A[45])
        # print(A[46])
        # print(A[47])
        # print(A[48])
        # print(A[49])
        # print(A[50])
        # print(A[51])
        # print(A[52])
        # print(A[53])
        # print(A[54])
        # print(A[55])
        # print(A[56])
        # print(A[57])
        # print(A[58])
        # print

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    #print(a)
    #print(a[-1]*a[-2])
    #print(a[0]*a[1])

    if a[-1]*a[-2] <= 0:
        if k <= n*(n-1)//2:
            print(0)
            return
        else:
            print(a[-1]*a[-2])
            return

    if a[0]*a[1] >= 0:
        if k <= n*(n-1)//2:
            print(a[0]*a[1])
            return
        else:
            print(0)
            return

    neg = []
    pos = []
    for i in range(n):
        if a[i] < 0:
            neg.append(a[i])
        else:
            pos.append(a[i])

    #print(neg)
    #print(pos)
    #print(len(neg))
    #print(len(pos))

    if len(neg) == 0 or len(pos) == 0:
        if k <= n*(n-1)//2:
            print(0)
            return
        else:
            print(a[-1]*a[-2])
            return

    if k <= len(neg)*len(pos):
        print(neg[0]*pos[-1])
        return
    else:
        #print(neg[0]*pos[-1])
        #print(neg[-1]*pos[0])
        print(max(neg[0]*pos[-1], neg[-1]*pos[0]))
        return

main()

=======
Suggestion 7

def problems155_d():
    pass

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += 1
            if ans == k:
                print(a[i]*a[j])
                exit()

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18-1
    r = 10**18+1
    while r-l > 1:
        m = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - bisect.bisect_left(a, m//a[i])
            elif a[i] > 0:
                cnt += bisect.bisect_right(a, m//a[i])
            else:
                if m >= 0:
                    cnt += n
        cnt //= 2
        if cnt < k:
            l = m
        else:
            r = m
    print(l)
