Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] != S[i - 1]:
            ans += 1
    if ans == 0:
        if S[0] == '0':
            print(0)
        else:
            print(N)
    else:
        print(min(ans + 2, N))

=======
Suggestion 2

def f(x, N, S, W):
    res = 0
    for i in range(N):
        if S[i] == '0' and W[i] < x:
            res += 1
        elif S[i] == '1' and W[i] >= x:
            res += 1
    return res

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    # print(N, S, W)
    # print(S.count('0'), S.count('1'))
    # print(W)
    def check(x):
        # print(x)
        cnt = 0
        for i in range(N):
            if S[i] == '0' and W[i] <= x:
                cnt += 1
            elif S[i] == '1' and W[i] > x:
                cnt += 1
        # print(cnt)
        return cnt
    def bin_search():
        left = -1
        right = 10**9+1
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid) >= N // 2 + 1:
                right = mid
            else:
                left = mid
        return right
    print(bin_search())

=======
Suggestion 4

def f(x):
    count = 0
    for i in range(n):
        if s[i] == "0":
            if w[i] < x:
                count += 1
        else:
            if w[i] >= x:
                count += 1
    return count

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    w = list(map(int,input().split()))
    #print(n,s,w)

    #print(s[0],w[0])
    #print(s[1],w[1])
    #print(s[2],w[2])
    #print(s[3],w[3])
    #print(s[4],w[4])

    #print(s[0] == '0')
    #print(s[1] == '0')
    #print(s[2] == '0')
    #print(s[3] == '0')
    #print(s[4] == '0')

    #print(s[0] == '1')
    #print(s[1] == '1')
    #print(s[2] == '1')
    #print(s[3] == '1')
    #print(s[4] == '1')

    #print(s[0] == '0' and w[0] < 50)
    #print(s[1] == '0' and w[1] < 50)
    #print(s[2] == '0' and w[2] < 50)
    #print(s[3] == '0' and w[3] < 50)
    #print(s[4] == '0' and w[4] < 50)

    #print(s[0] == '1' and w[0] >= 50)
    #print(s[1] == '1' and w[1] >= 50)
    #print(s[2] == '1' and w[2] >= 50)
    #print(s[3] == '1' and w[3] >= 50)
    #print(s[4] == '1' and w[4] >= 50)

    #print(s[0] == '0' and w[0] < 50 or s[0] == '1' and w[0] >= 50)
    #print(s[1] == '0' and w[1] < 50 or s[1] == '1' and w[1] >= 50)
    #print(s[2] == '0' and w[2] < 50 or s[2] == '1' and w[

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))

    # 0,1の数を数える
    count_zero = s.count('0')
    count_one = s.count('1')
    # print(count_zero, count_one)

    # 重さの小さい順にソート
    w.sort()
    # print(w)

    # 重さの小さい順に0,1の数を数える
    count_zero_list = []
    count_one_list = []
    tmp_zero = 0
    tmp_one = 0
    for i in range(n):
        if s[i] == '0':
            tmp_zero += 1
        else:
            tmp_one += 1
        count_zero_list.append(tmp_zero)
        count_one_list.append(tmp_one)
    # print(count_zero_list)
    # print(count_one_list)

    # 重さの小さい順に0,1を判定
    max_count = 0
    for i in range(n):
        # 0の数は、0,1の数から引く
        tmp_count_zero = count_zero_list[i] - count_zero
        # 1の数は、0,1の数から引く
        tmp_count_one = count_one_list[i] - count_one
        # print(tmp_count_zero, tmp_count_one)

        # 0,1の数の差の絶対値が最大のものを選ぶ
        tmp_max_count = max(abs(tmp_count_zero), abs(tmp_count_one))
        # print(tmp_max_count)

        # 重さの小さい順に判定しているため、最大値を超える場合は、最大値を更新する
        if tmp_max_count > max_count:
            max_count = tmp_max_count

    print(max_count)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # print(N, S, W)

    # 二分查找
    # 用于判断当前X下的人是儿童还是成年人
    def check(x):
        # 遍历所有人
        for s, w in zip(S, W):
            # 判断
            if s == '0' and w >= x:
                return True
            elif s == '1' and w < x:
                return True
        return False

    # 二分查找
    def binary_search():
        # 左右边界
        left = 0
        right = 10 ** 9 + 1
        # 循环
        while right - left > 1:
            # 中间值
            mid = (left + right) // 2
            # 判断
            if check(mid):
                left = mid
            else:
                right = mid
        # 返回
        return left

    # 输出
    print(binary_search())

=======
Suggestion 8

def judge(x):
    count = 0
    for i in range(N):
        if S[i] == '0' and W[i] < x:
            count += 1
    return count

N = int(input())
S = input()
W = list(map(int, input().split()))
left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if judge(mid) >= N // 2 + 1:
        right = mid
    else:
        left = mid
print(right)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W_sum = sum(W)
    W_cumsum = [0] * (N+1)
    for i in range(N):
        W_cumsum[i+1] = W_cumsum[i] + W[i]

    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans = max(ans, W_sum - W_cumsum[i+1])
        else:
            ans = max(ans, W_cumsum[i])

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))

    # 二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る
        # 条件式を書く
        #if arg >= 50:
        #    return True
        #else:
        #    return False
        # この場合は、argが50以上かどうかの条件式になる
        # 今回の場合は、arg以下の体重の人が儿童で、arg以上の体重の人が成年人であるという条件式になる
        # つまり、arg以下の体重の人の中で最大の体重がargとなるようなargを探す
        # そのため、arg以下の体重の人の中で最大の体重と、arg以上の体重の人の中で最小の体重が一致するようなargを探す
        # このようなargというのは、arg以下の体重の人の中で最大の体重をargとしたとき、arg以上の体重の人の中で最小の体重と一致するということは、
        # arg以上の体重の人の中で最小の体重をargとしたとき、arg以下の体重の人の中で最大の体重と一致するということになる
        # つまり、arg以下の体重の人の中で最大の体重と、arg以上の体重の人の中で最小の体重が一致するということは、argが条件を満たすということになる
        # このようなargは、arg以下の体重の人の中で最大の体重と、arg以上の体重の人の中で最小の体重が一
