Synthesizing 8/10 solutions

=======
Suggestion 1

def solve(n, k, p):
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] >= p[i]:
            if stack[-1][0] == p[i]:
                ans[stack[-1][1]] = i + 1
            stack.pop()
        stack.append((p[i], i))
        if len(stack) == k:
            for j in range(k):
                ans[stack[j][1]] = i + 1
            stack = []
    return ans

n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = solve(n, k, p)
for i in range(n):
    print(ans[i])

=======
Suggestion 2

def solve(n, k, p):
    # 从后往前遍历，如果当前的数比栈顶的数要大，就把栈顶的数弹出，直到当前的数比栈顶的数要小
    # 这样就可以保证栈内的数是从小到大排列的
    # 用一个栈来存储，栈内的数是从小到大排列的
    stack = []
    ans = [-1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        # 如果当前的数比栈顶的数要大，就把栈顶的数弹出，直到当前的数比栈顶的数要小
        while len(stack) > 0 and stack[-1][0] < p[i]:
            # 弹出栈顶的数，弹出的数的下标就是当前数的答案
            _, index = stack.pop()
            ans[index] = i + 1
        # 把当前的数和下标入栈
        stack.append((p[i], i))
    return ans

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
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
    # print(p.index(58))
    #

=======
Suggestion 4

def solve(n,k,p):
    # 为了能够使用bisect库，需要将牌的顺序倒过来
    p = p[::-1]
    # 用于存储每张牌被吃掉的步数
    ans = [0] * n
    # 用于存储桌子上的牌
    table = []
    # 用于存储桌子上的牌的最大值
    table_max = 0
    for i in range(n):
        # 将牌放在桌子上
        table.append(p[i])
        # 如果桌子上有k张牌，就吃掉
        if len(table) == k:
            # 用来存储被吃掉的牌
            eat = []
            # 从桌子上取出牌
            for j in range(k):
                # 如果牌的值大于等于当前桌子上的最大值，就吃掉
                if table[j] >= table_max:
                    eat.append(table[j])
            # 将被吃掉的牌从桌子上删除
            for e in eat:
                table.remove(e)
            # 更新桌子上的最大值
            if len(table) > 0:
                table_max = max(table)
            else:
                table_max = 0
        # 如果桌子上有牌，就将牌放在桌子上最小的牌上面
        if len(table) > 1:
            table.sort()
        # 计算牌被吃掉的步数
        ans[p[i]-1] = i+1
    # 将牌的顺序倒回去
    ans = ans[::-1]
    # 输出结果
    for a in ans:
        print(a)

=======
Suggestion 5

def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    ans = [-1]*N
    stack = []
    for i in range(N):
        while stack and stack[-1][0] >= P[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((P[i],i+1))
    for i in range(K):
        print(ans[i])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    cards = [0] * n
    for i in range(n):
        cards[i] = [p[i], i]
    cards.sort(key=lambda x: x[0])
    ans = [-1] * n
    for i in range(k):
        ans[cards[i][1]] = i + 1
    print(*ans, sep='\n')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 每张牌被吃掉的步数
    step = [-1] * N
    # 每张牌的位置
    position = [-1] * N
    for i in range(N):
        position[P[i]-1] = i

    # 当前桌面上的牌
    table = []
    for i in range(N):
        # 抽出的牌
        card = P[i]
        # 抽出的牌在桌面上的位置
        card_pos = position[card-1]

        # 抽出的牌放在桌面上
        table.append(card)
        # 抽出的牌在桌面上的位置
        table_pos = len(table) - 1

        # 如果桌面上有K张牌，吃掉
        if len(table) == K:
            for j in range(K):
                table.pop(0)

        # 抽出的牌的位置
        step[card-1] = card_pos - table_pos

    for i in range(N):
        print(step[i])

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(p)
    #print(n, k)
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
    #print(p[64])
    #print(p[65])
