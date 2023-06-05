Synthesizing 10/10 solutions

=======
Suggestion 1

def min_change(s, t):
    # s: str, t: str
    # return: int
    # 将s中的某些字符改变，使得t成为s的子串，求改变的最小字符数
    # 例如，将s中的第四个字符a改为c，就可以将s中的第二至第四个字符匹配到t
    # 由于s本身没有t作为它的子串，这个变化的数量--1--是最小的需要
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        return -1
    min_change_count = len_s
    for i in range(len_s - len_t + 1):
        change_count = 0
        for j in range(len_t):
            if s[i + j] != t[j]:
                change_count += 1
        if change_count < min_change_count:
            min_change_count = change_count
    return min_change_count

=======
Suggestion 2

def problem177_b():
    s = input()
    t = input()
    max = len(s)
    for i in range(len(s)):
        if len(s[i:i+len(t)]) < len(t):
            break
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < max:
            max = count
    print(max)

=======
Suggestion 3

def find_min_change(s, t):
    # s = list(s)
    # t = list(t)
    # print(s)
    # print(t)
    # s_len = len(s)
    # t_len = len(t)
    # if s_len < t_len:
    #     return -1
    # else:
    #     min_change = 0
    #     for i in range(t_len):
    #         if s[i] != t[i]:
    #             min_change += 1
    #     return min_change
    s = list(s)
    t = list(t)
    s_len = len(s)
    t_len = len(t)
    if s_len < t_len:
        return -1
    else:
        min_change = 0
        for i in range(s_len - t_len + 1):
            for j in range(t_len):
                if s[i + j] != t[j]:
                    min_change += 1
        return min_change

=======
Suggestion 4

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans,cnt)
    print(ans)
main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if min > count:
            min = count
    print(min)

=======
Suggestion 6

def get_min_change_num(str1, str2):
    """
    从str1中找出str2的最小子串，需要改变的字符数
    :param str1:
    :param str2:
    :return:
    """
    # 从str1中找出str2的最小子串，需要改变的字符数
    # 初始化
    min_change_num = 1000
    for i in range(len(str1)):
        print(i)
        for j in range(i+1, len(str1)):
            print(j)
            sub_str1 = str1[i:j]
            print(sub_str1)
            if str2 in sub_str1:
                print("str2 in sub_str1")
                change_num = len(sub_str1) - len(str2)
                if change_num < min_change_num:
                    min_change_num = change_num
    return min_change_num

=======
Suggestion 7

def solve():
    S = input()
    T = input()
    min = len(T)
    for i in range(0, len(S)-len(T)+1):
        count = 0
        for j in range(0, len(T)):
            if(S[i+j] != T[j]):
                count += 1
        if(count < min):
            min = count
    print(min)

solve()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    m = len(s)
    n = len(t)
    ans = n
    for i in range(m-n+1):
        cnt = 0
        for j in range(n):
            if t[j] != s[i+j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def get_min_change_num(S, T):
    min_change_num = len(S)
    for i in range(len(S) - len(T) + 1):
        change_num = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                change_num += 1
        if change_num < min_change_num:
            min_change_num = change_num
    return min_change_num

=======
Suggestion 10

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)-len(T)+1):
        s = S[i:i+len(T)]
        for j in range(len(T)):
            if s[j] != T[j]:
                count += 1
    print(count)

main()
