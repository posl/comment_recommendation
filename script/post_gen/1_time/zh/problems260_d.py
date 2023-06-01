Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = -1
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1][0] >= p[i]:
            stack.pop()
        if len(stack) > 0:
            ans[i] = stack[-1][1]
        stack.append((p[i], i+1))
        if len(stack) == k:
            stack.pop(0)
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = [-1]*n
    t = 0
    for i in range(n):
        while t>0 and p[i]>p[ans[t-1]]:
            t -= 1
        ans[t] = i
        t += 1
        if t == k:
            for j in range(k):
                ans[j] = -1
            t = 0

    for i in range(n):
        print(ans[i]+1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #p = [3, 14, 15, 9, 2, 6, 5, 13, 1, 7, 10, 11, 8, 12, 4]
    #n,k = 15,3
    #p = [1, 2, 3, 4, 5]
    #n,k = 5,1
    #p = [3, 5, 2, 1, 4]
    #n,k = 5,2
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,2
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,1
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,200000

    #print(p)
    #print(n,k)
    #print(len(p))
    #print(len(set(p)))

    #p = [3, 14, 15, 9, 2, 6, 5, 13, 1, 7, 10, 11, 8, 12, 4]
    #n,k = 15,3
    #p = [1, 2, 3, 4, 5]
    #n,k = 5,1
    #p = [3, 5, 2, 1, 4]
    #n,k = 5,2
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,2
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,1
    #p = [i for i in range(1,n+1)]
    #n,k = 200000,200000

    #print(p)
    #print(n,k)
    #print(len(p))
    #print(len(set(p)))

    #p = [3, 14, 15, 9, 2, 6, 5, 13, 1,

=======
Suggestion 4

def solve(n, k, p):
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] > p[i]:
            stack.pop()
        if stack and stack[-1][1] >= k:
            ans[i] = stack[-1][2]
        else:
            ans[i] = -1
        stack.append((p[i], i+1, ans[i]))
    return ans

n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = solve(n, k, p)
for i in range(n):
    print(ans[i])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
    # print(n, k, cards)
    # 1. cards中每个元素的索引值就是牌的数字，值就是牌的位置
    # 2. 用一个列表记录每个牌的位置
    # 3. 用一个列表记录每个牌是否被吃掉
    # 4. 用一个列表记录每个牌被吃掉的步数
    cards_position = [0] * (n + 1)
    cards_eaten = [False] * (n + 1)
    cards_eaten_step = [0] * (n + 1)
    for i in range(1, n + 1):
        cards_position[cards[i - 1]] = i
    # print(cards_position)
    for i in range(1, n + 1):
        if cards_eaten[i]:
            continue
        # print(i)
        cards_eaten[i] = True
        cards_eaten_step[i] = 0
        cards_eaten_count = 1
        next_card = cards_position[i]
        # print(next_card)
        while next_card != i:
            if cards_eaten[next_card]:
                break
            cards_eaten[next_card] = True
            cards_eaten_count += 1
            cards_eaten_step[next_card] = cards_eaten_step[i] + cards_eaten_count
            next_card = cards_position[next_card]
    # print(cards_eaten_step)
    for i in range(1, n + 1):
        print(cards_eaten_step[i])

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    #print(N,K,P)
    #print(P.index(3))
    #print(P.index(3,3))
    #print(P.index(3,6))
    #print(P.index(3,9))
    #print(P.index(3,12))
    #print(P.index(3,15))
    #print(P.index(3,18))
    #print(P.index(3,21))
    #print(P.index(3,24))
    #print(P.index(3,27))
    #print(P.index(3,30))
    #print(P.index(3,33))
    #print(P.index(3,36))
    #print(P.index(3,39))
    #print(P.index(3,42))
    #print(P.index(3,45))
    #print(P.index(3,48))
    #print(P.index(3,51))
    #print(P.index(3,54))
    #print(P.index(3,57))
    #print(P.index(3,60))
    #print(P.index(3,63))
    #print(P.index(3,66))
    #print(P.index(3,69))
    #print(P.index(3,72))
    #print(P.index(3,75))
    #print(P.index(3,78))
    #print(P.index(3,81))
    #print(P.index(3,84))
    #print(P.index(3,87))
    #print(P.index(3,90))
    #print(P.index(3,93))
    #print(P.index(3,96))
    #print(P.index(3,99))
    #print(P.index(3,102))
    #print(P.index(3,105))
    #print(P.index(3,108))
    #print(P.index(3,111))
    #print(P.index(3,114))
    #print(P.index(3,117))
    #print(P.index(3,120))
    #print(P.index(3,123))
    #print(P.index(3,126))
    #print(P.index(3,129))
    #print(P.index(3,132))
    #print(P.index(3,135))
    #print(P.index(3,138))
    #print

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    # 位置i的牌，被吃掉的时间
    ans = [-1]*n
    # 桌面上的牌
    table = []
    # 桌面上的牌的最小值
    min_table = float('inf')
    for i in range(n):
        # 抽出的牌的值
        x = p[i]
        # 抽出的牌的位置
        x_pos = i+1
        # 如果桌面上有牌
        if table:
            # 如果抽出的牌的值大于桌面上的牌的最小值
            if x > min_table:
                # 将抽出的牌放到桌面上，不叠加在任何牌上
                table.append(x)
            else:
                # 将抽出的牌放到桌面上，叠加在最小值上
                table.append(x)
                # 桌面上的牌的最小值更新
                min_table = x
                # 如果桌面上的牌的数量大于k
                if len(table) > k:
                    # 抽出的牌被吃掉
                    ans[x_pos-1] = i-k+1
                    # 桌面上的牌的最小值更新
                    min_table = min(table[-k:])
        else:
            # 将抽出的牌放到桌面上，不叠加在任何牌上
            table.append(x)
        # 如果桌面上的牌的数量大于k
        if len(table) > k:
            # 抽出的牌被吃掉
            ans[x_pos-1] = i-k+1
            # 桌面上的牌的最小值更新
            min_table = min(table[-k:])
    # 输出答案
    for i in range(n):
        print(ans[i])

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # print(n, k)
    # print(p)
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
Suggestion 9

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
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
    #print(p.index(58))
    #print(p.index(59
