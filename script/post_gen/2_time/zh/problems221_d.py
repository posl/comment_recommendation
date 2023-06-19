Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(max(A

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dict = {}
    for i in range(N):
        for j in range(A[i], A[i] + B[i]):
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1

    ans = [0] * N
    for i in dict.values():
        ans[i - 1] += 1

    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    n=int(input())
    a,b=[],[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    ans=[0]*n
    for i in range(n):
        ans[0]+=1
        if i!=n-1:
            ans[i+1]-=1
    for i in range(n-1):
        ans[i+1]+=ans[i]
    for i in range(n):
        print(ans[i],end=' ')
    print()
main()

=======
Suggestion 4

def problems221_d():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [0]*(10**9+1)
    for i in range(n):
        c[a[i]] += 1
        c[a[i]+b[i]] -= 1
    for i in range(1, 10**9+1):
        c[i] += c[i-1]
    d = [0]*(n+1)
    for i in range(1, 10**9+1):
        if c[i] > 0:
            d[c[i]] += 1
    for i in range(1, n+1):
        print(d[i], end=' ')

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # print(a)
    # print(b)
    # print("")

    # for i in range(n):
    #     print(str(a[i]) + " " + str(b[i]))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))

    # print("")

    l = []
    for i in range(n):
        l.append([a[i] + b[i] - 1, a[i] - 1])

    # print(l)
    # print("")

    l.sort()

    # print(l)
    # print("")

    # for i in range(n):
    #     print(str(l[i][0]) + " " + str(l[i

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(N):
        B.append(A[i][0])
        B.append(A[i][0] + A[i][1])
    B.sort()
    C = []
    for i in range(2 * N - 1):
        C.append(B[i + 1] - B[i])
    D = [0] * N
    for i in range(2 * N - 1):
        if C[i] != 0:
            D[C[i] - 1] += 1
    for i in range(N):
        print(D[i], end = ' ')

=======
Suggestion 7

def main():
    import sys
    from operator import itemgetter
    from itertools import accumulate
    from bisect import bisect_left

    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]

    # 始点と終点をそれぞれ切り出す
    a, b = map(list, zip(*ab))

    # 終点を昇順にソート
    b.sort()

    # 終点を累積和に変換
    # 例えば [1, 2, 3] なら [1, 3, 6]
    b = list(accumulate(b))

    # 各始点について、終点の累積和から始点より小さい最大の終点のインデックスを求める
    # 例えば [1, 2, 3] なら [0, 0, 1]
    # 例えば [1, 3, 6] なら [0, 0, 1]
    c = [bisect_left(b, x) for x in a]

    # 0 ～ N-1 のインデックスについて、終点の累積和からそのインデックスより小さい最大の終点のインデックスを引く
    # 例えば [0, 0, 1] なら [1, 1, 0]
    # 例えば [0, 0, 1] なら [1, 1, 0]
    d = [b[x] - x for x in c]

    # 0 ～ N-1 のインデックスについて、終点の累積和からそのインデックスより小さい最大の終点のインデックスを引く
    # 例えば [1, 1, 0] なら [1, 1, 0]
    # 例えば [1, 1, 0] なら [1, 1, 0]

=======
Suggestion 8

def solve():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] + B[i] - 1
    ans.sort()
    for i in range(N):
        print(ans[i], end=' ')
    print()

=======
Suggestion 9

def main():
    n = int(input())
    l = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append([a,b])
    l.sort()
    print(l)
    l2 = []
    for i in range(n):
        l2.append(l[i][0])
        l2.append(l[i][0]+l[i][1])
    print(l2)
    l3 = [0]*(max(l2)+1)
    print(l3)
    for i in l2:
        l3[i] += 1
    print(l3)
    l4 = [0]*(n+1)
    for i in l3:
        l4[i] += 1
    print(l4)
    for i in range(1,n+1):
        print(l4[i],end=" ")
    print()

=======
Suggestion 10

def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B
