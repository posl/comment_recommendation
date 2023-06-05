Synthesizing 10/10 solutions

=======
Suggestion 1

def func(x, n, p):
    # x: number on the card
    # n: number of cards
    # p: permutation of the cards
    # return: the step that the card is eaten
    #print("func({},{},{})".format(x, n, p))
    #print("p[x-1]:{}".format(p[x-1]))
    if p[x-1] == 1:
        return 1
    else:
        return func(p[x-1], n, p) + 1

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = [int(i) for i in input().split()]
    # print(n, k, p)
    # print(p.index(1))
    # print(p.index(2))
    # print(p.index(3))
    # print(p.index(4))
    # print(p.index(5))
    # print(p.index(6))
    # print(p.index(7))
    # print(p.index(8))
    # print(p.index(9))
    # print(p.index(10))
    # print(p.index(11))
    # print(p.index(12))
    # print(p.index(13))
    # print(p.index(14))
    # print(p.index(15))
    # print(p.index(16))
    # print(p.index(17))
    # print(p.index(18))
    # print(p.index(19))
    # print(p.index(20))
    # print(p.index(21))
    # print(p.index(22))
    # print(p.index(23))
    # print(p.index(24))
    # print(p.index(25))
    # print(p.index(26))
    # print(p.index(27))
    # print(p.index(28))
    # print(p.index(29))
    # print(p.index(30))
    # print(p.index(31))
    # print(p.index(32))
    # print(p.index(33))
    # print(p.index(34))
    # print(p.index(35))
    # print(p.index(36))
    # print(p.index(37))
    # print(p.index(38))
    # print(p.index(39))
    # print(p.index(40))
    # print(p.index(41))
    # print(p.index(42))
    # print(p.index(43))
    # print(p.index(44))
    # print(p.index(45))
    # print(p.index(46))
    # print(p.index(47))
    # print(p.index(48))
    # print(p.index(49))
    # print(p.index(50))
    # print(p.index(51))
    # print(p.index(52))
    # print(p.index(53))
    # print(p.index(54))
    # print(p.index(55))
    # print(p.index(56))
    # print(p.index(57))
    # print(p.index(58

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = [0] * n
    r = [0] * n
    for i in range(n):
        q[p[i]-1] = i
    for i in range(n):
        if i < k:
            r[i] = i
        else:
            r[i] = max(r[i-k], q[i])
    for i in range(n):
        if r[i] == n-1:
            print(-1)
        else:
            print(r[i]+2)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    #print(p)
    #print(p.index(1))
    #print(p.index(2))
    #print(p.index(3))
    #print(p.index(4))
    #print(p.index(5))
    #print(p.index(6))
    #print(p.index(7))
    #print(p.index(8))
    #print(p.index(9))
    #print(p.index(10))
    #print(p.index(11))
    #print(p.index(12))
    #print(p.index(13))
    #print(p.index(14))
    #print(p.index(15))
    #print(p.index(16))
    #print(p.index(17))
    #print(p.index(18))
    #print(p.index(19))
    #print(p.index(20))
    #print(p.index(21))
    #print(p.index(22))
    #print(p.index(23))
    #print(p.index(24))
    #print(p.index(25))
    #print(p.index(26))
    #print(p.index(27))
    #print(p.index(28))
    #print(p.index(29))
    #print(p.index(30))
    #print(p.index(31))
    #print(p.index(32))
    #print(p.index(33))
    #print(p.index(34))
    #print(p.index(35))
    #print(p.index(36))
    #print(p.index(37))
    #print(p.index(38))
    #print(p.index(39))
    #print(p.index(40))
    #print(p.index(41))
    #print(p.index(42))
    #print(p.index(43))
    #print(p.index(44))
    #print(p.index(45))
    #print(p.index(46))
    #print(p.index(47))
    #print(p.index(48))
    #print(p.index(49))
    #print(p.index(50))
    #print(p.index(51))
    #print(p.index(52))
    #print(p.index(53))
    #print(p.index(54))
    #print(p.index(55))
    #print(p.index(56))
    #print(p.index(57))
    #print(p.index

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    ans[0] = 1
    for i in range(n):
        if i == 0:
            continue
        ans[i] = ans[p[i] - 1] + 1
    for i in range(n):
        if ans[i] > k:
            ans[i] = -1
    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 各カードの位置を記録
    card_pos = [0] * N
    for i in range(N):
        card_pos[P[i]-1] = i

    # 各カードが何回目に消えるかを記録
    card_eat = [-1] * N
    for i in range(N):
        # カードが消えていない場合
        if card_eat[i] == -1:
            # カードの位置を記録
            pos = card_pos[i]
            # 消えるカードの数を数える
            eat_cnt = 0
            while True:
                # カードが消えている場合
                if card_eat[P[pos]-1] != -1:
                    break
                # カードを消す
                card_eat[P[pos]-1] = i+1
                # 消えるカードの数を増やす
                eat_cnt += 1
                # カードの位置を進める
                pos += K
                # カードの位置が範囲外の場合
                if pos >= N:
                    pos -= N
            # 消えるカードの数を記録
            for j in range(eat_cnt):
                card_eat[P[pos]-1] = i+1

    # 結果を出力
    for i in range(N):
        print(card_eat[i])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    #print(p.index(1))
    #print(p[p.index(1)])
    #print(p[0])
    #print(p[1])
    #print(p[2])
    #print(p[3])
    #print(p[4])
    #print(p[5])
    #print(p[6])
    #print(p[7])
    #print(p[8])
    #print(p[9])
    #print(p[10])
    #print(p[11])
    #print(p[12])
    #print(p[13])
    #print(p[14])
    #print(p[15])
    #print(p[16])
    #print(p[17])
    #print(p[18])
    #print(p[19])
    #print(p[20])
    #print(p[21])
    #print(p[22])
    #print(p[23])
    #print(p[24])
    #print(p[25])
    #print(p[26])
    #print(p[27])
    #print(p[28])
    #print(p[29])
    #print(p[30])
    #print(p[31])
    #print(p[32])
    #print(p[33])
    #print(p[34])
    #print(p[35])
    #print(p[36])
    #print(p[37])
    #print(p[38])
    #print(p[39])
    #print(p[40])
    #print(p[41])
    #print(p[42])
    #print(p[43])
    #print(p[44])
    #print(p[45])
    #print(p[46])
    #print(p[47])
    #print(p[48])
    #print(p[49])
    #print(p[50])
    #print(p[51])
    #print(p[52])
    #print(p[53])
    #print(p[54])
    #print(p[55])
    #print(p[56])
    #print(p[57])
    #print(p[58])
    #print(p[59])
    #print(p[60])
    #print(p[61])
    #print(p[62])
    #print(p[63])

=======
Suggestion 8

def solve(n, k, p):
    # 桌子上的牌
    table = []
    # 从上面抽出的牌
    card = []
    # 每张牌被吃掉的步数
    ans = [-1] * n
    # 初始化桌子
    for i in range(n):
        table.append(i + 1)
    # 初始化抽出的牌
    for i in range(n):
        card.append(p[i])
    # 从上面抽出的牌的位置
    pos = 0
    # 抽牌
    for i in range(n):
        # 抽出的牌
        c = card[i]
        # 抽出的牌的位置
        pos = c - 1
        # 抽出的牌的上面的牌
        top = table[pos]
        # 如果桌面上没有牌或者桌面上的牌比抽出的牌大，就把抽出的牌放在桌面上
        if len(table) == 0 or top > c:
            table.append(c)
        # 否则，就把抽出的牌放在桌面上最上面的那张牌上
        else:
            table[top - 1] = c
        # 把桌面上的牌按照从小到大排序
        table.sort()
        # 如果桌面上有k张牌，就把桌面上的牌吃掉
        if len(table) >= k:
            for j in range(k):
                # 把桌面上最小的k张牌吃掉
                ans[table[j] - 1] = i + 1
            # 把桌面上最小的k张牌从桌面上去掉
            table = table[k:]
    # 输出
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.insert(0,0)
    stack = []
    ans = [-1]*(n+1)
    for i in range(1,n+1):
        while stack and p[i] <= p[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    for i in range(n):
        print(ans[i+1])

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    ans = [-1]*n
    for i in range(n):
        if ans[i] != -1:
            continue
        x = i
        cnt = 0
        while True:
            cnt += 1
            ans[x] = cnt
            x = p[x]-1
            if ans[x] != -1:
                break
    for i in range(n):
        if ans[i] <= k:
            print(ans[i])
        else:
            print(-1)
