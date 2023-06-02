Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        cards.append(list(map(int, input().split())))
    # print(cards)
    # cards = [[1, 4], [2, 3], [5, 7]]
    # cards = [[2, 8], [9, 3], [4, 11], [5, 1], [12, 6]]
    # N = 5
    # S = 25
    # print(cards)
    # print(N, S)
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    # print(cards[4][1])
    # print(cards[5][0])
    # print(cards[5][1])

    # 1. 确定是否有解
    # 2. 如果有解，输出解
    # 3. 如果有多个解，输出任意一个解
    # 4. 如果没有解，输出No

    # 1. 确定是否有解
    # 1.1. 确定是否有解
    # 1.2. 如果有解，输出解
    # 1.3. 如果有多个解，输出任意一个解
    # 1.4. 如果没有解，输出No
    # 1.1. 确定是否有解
    # 1.1.1. 确定是否有解
    # 1.1.2. 如果有解，输出解
    # 1.1.3. 如果有多个解，输出任意一个解
    # 1.1.4. 如果没有解，输出No
    # 1.1.1. 确定是否有解
    #

=======
Suggestion 2

def solve(n,s,card):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if ((i >> j) & 1):
                sum += card[j][0]
            else:
                sum += card[j][1]
        if sum == s:
            return True,i
    return False,0

=======
Suggestion 3

def is_sum_possible(a, b, s):
    if s == 0:
        return True
    if len(a) == 0:
        return False

    return is_sum_possible(a[1:], b[1:], s) or is_sum_possible(a[1:], b[1:], s-a[0]-b[0]) or is_sum_possible(a[1:], b[1:], s-a[0]) or is_sum_possible(a[1:], b[1:], s-b[0])

=======
Suggestion 4

def solve(n,s,ab):
    #ab = [(1,4),(2,3),(5,7)]
    #n,s = 3,11
    for i in range(2**n):
        #print(i)
        a = []
        for j in range(n):
            if (i>>j)&1:
                a.append(ab[j][0])
            else:
                a.append(ab[j][1])
        #print(a)
        if sum(a) == s:
            print("Yes")
            for j in range(n):
                if (i>>j)&1:
                    print("T",end="")
                else:
                    print("H",end="")
            print()
            return
    print("No")
    return

=======
Suggestion 5

def dfs(i, sum):
    global N
    global S
    global a
    global b
    global ans
    if i == N:
        if sum == S:
            ans = True
        return
    dfs(i+1, sum+a[i])
    dfs(i+1, sum+b[i])

N, S = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

ans = False
dfs(0, 0)

=======
Suggestion 6

def find_sum(n, s, a, b):
    if n == 1:
        if a[0] == s or b[0] == s:
            return True
        else:
            return False
    else:
        for i in range(n):
            if a[i] + b[i] == s:
                return True
            else:
                for j in range(i+1, n):
                    if a[i] + a[j] == s:
                        return True
                    if b[i] + b[j] == s:
                        return True
    return False

=======
Suggestion 7

def func(n, s, a, b):
    for i in range(n):
        if a[i] == s or b[i] == s:
            print("Yes")
            print("T" * i + "H" + "T" * (n - i - 1))
            return
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == s or a[i] + b[j] == s or b[i] + a[j] == s or b[i] + b[j] == s:
                print("Yes")
                if a[i] + a[j] == s:
                    print("T" * i + "TT" + "T" * (j - i - 1) + "H" + "T" * (n - j - 1))
                    return
                if a[i] + b[j] == s:
                    print("T" * i + "TH" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
                if b[i] + a[j] == s:
                    print("T" * i + "HT" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
                if b[i] + b[j] == s:
                    print("T" * i + "HH" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
    print("No")

n, s = map(int, input().split())
a = []
b = []
for i in range(n):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
func(n, s, a, b)

=======
Suggestion 8

def dfs(i, sum):
    if i == n:
        if sum == S:
            return True
        else:
            return False
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum+a[i]):
        return True
    return False

=======
Suggestion 9

def dfs(i, sum):
    if i == n:
        return sum == S
    if dfs(i + 1, sum + a[i]):
        return True
    if dfs(i + 1, sum):
        return True
    return False

n, S = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

=======
Suggestion 10

def main():
    N,S = map(int,input().split())
    a,b = [],[]
    for i in range(N):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)

    # print(N,S,a,b)
    # print(sum(a))
    # print(sum(b))
    if S > sum(a) and S > sum(b):
        print("No")
        return

    if S == sum(a):
        print("Yes")
        print("".join(["H" for i in range(N)]))
        return

    if S == sum(b):
        print("Yes")
        print("".join(["T" for i in range(N)]))
        return

    if S < sum(a):
        # print("a")
        # print(a)
        # print(b)
        # print(S)
        for i in range(N):
            if a[i] == S:
                print("Yes")
                print("".join(["H" for i in range(i)] + ["T" for i in range(i,N)]))
                return
            elif a[i] < S:
                S -= a[i]
            else:
                print("No")
                return
        print("No")
        return

    if S < sum(b):
        # print("b")
        # print(a)
        # print(b)
        # print(S)
        for i in range(N):
            if b[i] == S:
                print("Yes")
                print("".join(["T" for i in range(i)] + ["H" for i in range(i,N)]))
                return
            elif b[i] < S:
                S -= b[i]
            else:
                print("No")
                return
        print("No")
        return
