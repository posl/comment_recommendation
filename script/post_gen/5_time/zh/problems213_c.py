Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(h, w, n, ab):
    #print(h, w, n, ab)
    #print(ab[0][0], ab[0][1])
    #print(ab[1][0], ab[1][1])
    #print(ab[2][0], ab[2][1])
    #print(ab[3][0], ab[3][1])
    #print(ab[4][0], ab[4][1])
    #print(ab[5][0], ab[5][1])
    #print(ab[6][0], ab[6][1])
    #print(ab[7][0], ab[7][1])
    #print(ab[8][0], ab[8][1])
    #print(ab[9][0],

=======
Suggestion 2

def main():
    h,w,n = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    #print(cards)
    #cards.sort(key=lambda x: x[0], reverse=True)
    #cards.sort(key=lambda x: x[1], reverse=True)
    #print(cards)
    #print(cards[0][0],cards[0][1])
    #print(cards[1][0],cards[1][1])
    #print(cards[2][0],cards[2][1])
    #print(cards[3][0],cards[3][1])
    #print(cards[4][0],cards[4][1])
    #print(cards[5][0],cards[5][1])
    #print(c

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve(h,w,n,ab):
    return 0

=======
Suggestion 5

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    A.sort()
    B = list(set(B))
    B.sort()
    for i in range(N):
        a = A.index(A[i]) + 1
        b = B.index(B[i]) + 1
        print(a, b)

=======
Suggestion 6

def main():
    """
    #思路：
    #1.先读取输入数据，存入列表中
    #2.遍历列表，找出每张数字牌的位置
    #3.打印每张数字牌的位置
    """
    #1.先读取输入数据，存入列表中
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    #2.遍历列表，找出每张数字牌的位置
    #初始化一个列表，用于存储每张数字牌的位置
    c = [0 for i in range(n)]
    d = [0 for i in range(n)]
    #遍历列表，找出每张数字牌的位置
    for i in range(n):
        #如果当前行没有数字牌
        if a.count(a[i]) == 1:
            #将当前行的所有牌拿掉
            for j in range(n):
                if a[j] == a[i]:
                    a[j] = 0
            #将剩下的牌往上移，填补这个空缺
            for j in range(n):
                if a[j] > a[i]:
                    a[j] -= 1
        #如果当前列没有数字牌
        if b.count(b[i]) == 1:
            #将当前列的所有牌拿掉
            for j in range(n):
                if b[j] == b[i]:
                    b[j] = 0
            #将剩下的牌往左移，以填补这个缺口
            for j in range(n):
                if b[j] > b[i]:
                    b[j] -= 1
        #找出每张数字牌的位置
        c[i] = a[i]
        d[i] = b[i]

    #3.打印每张数字牌的位置
    for i in range(n):
        print(c[i], d[i])

=======
Suggestion 7

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append((a1, i))
        b.append((b1, i))
    a.sort()
    b.sort()
    a1 = 0
    b1 = 0
    a2 = 0
    b2 = 0
    for i in range(n):
        if a[i][0] != a1:
            a2 += 1
        if b[i][0] != b1:
            b2 += 1
        a1 = a[i][0]
        b1 = b[i][0]
        a[i] = (a[i][1], a2)
        b[i] = (b[i][1], b2)
    a.sort()
    b.sort()
    for i in range(n):
        print(a[i][1], b[i][1])

main()

=======
Suggestion 8

def main():
    H, W, N = map(int, input().split())
    cards = []
    for i in range(N):
        A, B = map(int, input().split())
        cards.append([A, B, i+1])
    cards.sort(key=lambda x: x[0])
    for i in range(N):
        cards[i][0] = i + 1
    cards.sort(key=lambda x: x[1])
    for i in range(N):
        cards[i][1] = i + 1
    cards.sort(key=lambda x: x[2])
    for i in range(N):
        print(cards[i][0], cards[i][1])
    return 0

=======
Suggestion 9

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # print(A)
    # print(B)
    # print(H, W, N)

    #将A, B中的数字进行排序，得到C, D
    C = sorted(A)
    D = sorted(B)

    # print(C)
    # print(D)

    #将C, D中的数字进行重新编号，得到E, F
    E = []
    F = []
    for i in range(N):
        E.append(C.index(A[i])+1)
        F.append(D.index(B[i])+1)

    # print(E)
    # print(F)

    #将E, F中的数字进行输出，得到G, H
    G = []
    H = []
    for i in range(N):
        G.append(str(E[i]))
        H.append(str(F[i]))

    # print(G)
    # print(H)

    #将G, H中的数字进行输出，得到I
    I = []
    for i in range(N):
        I.append(G[i] + " " + H[i])

    # print(I)

    #将I中的数字进行输出
    for i in range(N):
        print(I[i])
