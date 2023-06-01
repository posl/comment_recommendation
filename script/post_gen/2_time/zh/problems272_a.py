Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(i, sum):
    if i == n:
        if sum == S:
            return True
        else:
            return False
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum + a[i]):
        return True
    return False

n, S = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

=======
Suggestion 2

def solve(n, s, a, b):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j]
            else:
                sum += b[j]
        if sum == s:
            return True, i
    return False, -1

=======
Suggestion 3

def dfs(i, sum):
    if i == n:
        return sum == S
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum + a[i]):
        return True
    return False

n, S = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print(a)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except:
            break
    return input_list

=======
Suggestion 6

def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    # print(cards)

    # 先计算正面和背面的和
    sum_front = 0
    sum_back = 0
    for i in range(N):
        sum_front += cards[i][0]
        sum_back += cards[i][1]
    # print(sum_front, sum_back)

    # 如果两个和都小于S，那么一定不可能
    if sum_front < S and sum_back < S:
        print("No")
        return

    # 如果两个和都大于S，那么一定不可能
    if sum_front > S and sum_back > S:
        print("No")
        return

    # 如果两个和中有一个等于S，那么一定可以
    if sum_front == S or sum_back == S:
        print("Yes")
        if sum_front == S:
            for i in range(N):
                print("H", end="")
        else:
            for i in range(N):
                print("T", end="")
        print("")
        return

    # 接下来就是sum_front < S and sum_back > S 或者 sum_front > S and sum_back < S
    # 那么就要分别考虑正面和背面的情况
    # sum_front < S and sum_back > S
    if sum_front < S and sum_back > S:
        # 正面的和肯定要小于S
        # 从大到小排列，先排正面
        cards.sort(key=lambda x: x[0], reverse=True)
        # print(cards)
        # 从大到小排列，再排背面
        cards.sort(key=lambda x: x[1], reverse=True)
        # print(cards)
        # 从前往后排列
        for i in range(N):
            if sum_front + cards[i][1] >= S:
                print("Yes")
                for j in range(i):
                    print("T", end="")
                print("H", end="")
                for j in range(i+1, N):
                    print("T", end="")

=======
Suggestion 7

def main():
    N, S = map(int, input().split())
    card = []
    for i in range(N):
        card.append(list(map(int, input().split())))
    if S == 0:
        print("Yes")
        print("T"*N)
        return
    for i in range(2**N):
        s = 0
        a = []
        for j in range(N):
            if (i>>j)&1:
                s += card[j][0]
                a.append("H")
            else:
                s += card[j][1]
                a.append("T")
        if s == S:
            print("Yes")
            print("".join(a))
            return
    print("No")

=======
Suggestion 8

def solve(N, S, A):
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1 == 1:
                sum += A[j][0]
            else:
                sum += A[j][1]
        if sum == S:
            return i
    return -1

=======
Suggestion 9

def main():
    n,s = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]

    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if i & (1<<j):
                    print("H",end="")
                else:
                    print("T",end="")
            print()
            return
    print("No")
