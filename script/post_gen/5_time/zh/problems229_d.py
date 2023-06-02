Synthesizing 10/10 solutions

=======
Suggestion 1

def problems229_d():
    pass

=======
Suggestion 2

def main():
    s = input()
    k = int(input())

    ans = 0
    cnt = 0
    for c in s:
        if c == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)

    ans += k * 2
    ans = min(ans, len(s))

    print(ans)

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    n = len(S)
    S = S + S
    start = 0
    end = 0
    cnt = 0
    ans = 0
    for i in range(n):
        if S[i] == "X":
            end += 1
        else:
            if cnt < K:
                end += 1
                cnt += 1
            else:
                while S[start] == "X":
                    start += 1
                start += 1
                end += 1
        ans = max(ans, end - start)
    print(ans)

=======
Suggestion 4

def main():
    # input
    S = input()
    K = int(input())

    # initialization
    N = len(S)
    S = S + 'X'
    cnt = 0
    ans = 0

    # count the number of X
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 0
    ans += cnt // 2

    # output
    print(min(ans + K, N - 1))

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    ans = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    ans += K
    ans = min(ans, len(S))
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    k = int(input())

    # 算法
    # 1. 找出连续最长的X的长度
    # 2. 计算可以替换的X的个数
    # 3. 计算最终结果
    # 注意：当k大于等于可以替换的X的个数时，结果为字符串的长度
    #       当k小于可以替换的X的个数时，结果为连续最长的X的长度加上k

    # 1. 找出连续最长的X的长度
    max_x = 0
    tmp_max_x = 0
    for c in s:
        if c == 'X':
            tmp_max_x += 1
        else:
            max_x = max(max_x, tmp_max_x)
            tmp_max_x = 0
    max_x = max(max_x, tmp_max_x)

    # 2. 计算可以替换的X的个数
    count_x = 0
    for c in s:
        if c == 'X':
            count_x += 1
    replace_x = count_x - max_x

    # 3. 计算最终结果
    if replace_x <= k:
        print(len(s))
    else:
        print(max_x + k)

=======
Suggestion 7

def solve():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    ans += 2 * k
    print(min(ans, n - 1))

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    s = s.replace(".", " ")
    s = s.split()
    s = [len(x) for x in s]
    s.sort(reverse = True)
    print(s[0] + s[1] + k)

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    n = len(s)
    if k >= n:
        print(n)
        return
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(k):
        if s[i] == 'X':
            ans -= 1
    for i in range(k, n):
        if s[i] == 'X':
            ans -= 1
        if s[i - k] == 'X':
            ans += 1
        if ans > k:
            ans = k
            break
    print(ans)

=======
Suggestion 10

def main():
    # 输入
    S = input()
    K = int(input())

    # 处理
    # 用 . 分割 S
    # 用列表存储分割后的结果
    s_list = S.split('.')
    # 用列表存储每个 . 之间的 X 的数量
    x_list = []
    for i in s_list:
        x_list.append(len(i))

    # 如果 s_list[0] 为空，说明 s_list[0] 前面没有 X，所以删除 x_list[0]
    if x_list[0] == 0:
        x_list.pop(0)
    # 如果 s_list[-1] 为空，说明 s_list[-1] 后面没有 X，所以删除 x_list[-1]
    if x_list[-1] == 0:
        x_list.pop(-1)

    # 如果没有 X，输出 0
    if len(x_list) == 0:
        print(0)
        exit()

    # 如果 K 大于等于 len(x_list)，说明可以将所有的 . 都替换为 X
    if K >= len(x_list):
        print(len(S))
        exit()

    # 如果 K 小于 len(x_list)，说明可以将 K 个 . 都替换为 X
    # 但是这 K 个 . 不能相邻，否则会有 K+1 个连续的 X
    # 所以将 K 个 . 替换为 X 后，会有 K+1 个连续的 X
    # 所以最多有 K+1 个连续的 X
    # 所以输出 K+1
    if K < len(x_list):
        print(K+1)
        exit()
