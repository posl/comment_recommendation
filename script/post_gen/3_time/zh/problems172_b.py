Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    # 用于存储字母的位置
    s_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = [i]
        else:
            s_dict[s[i]].append(i)
    # print(s_dict)
    # 用于存储字母的位置
    t_dict = {}
    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = [i]
        else:
            t_dict[t[i]].append(i)
    # print(t_dict)
    # 用于存储不同字母的位置
    diff = []
    for i in range(len(s)):
        if s[i] != t[i]:
            diff.append(i)
    # print(diff)
    # 用于记录不同字母的位置是否相同
    flag = True
    for i in diff:
        if s[i] not in t_dict or t[i] not in s_dict:
            flag = False
            break
        elif s_dict[s[i]] != t_dict[t[i]]:
            flag = False
            break
    if flag:
        print(1)
    else:
        print(2)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print(0)
        return
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    i = 0
    while i < len(s) and i < len(t):
        if s[i] != t[i]:
            break
        i += 1
    print(len(s) - i + len(t) - i)

=======
Suggestion 5

def solve():
    # 解题算法
    S = input()
    T = input()
    if S == T:
        return 0
    ans = 10**5
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        ans = min(ans, count)
    return ans

=======
Suggestion 6

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

main()

=======
Suggestion 7

def main():
    s = input()
    t = input()
    # print(s)
    # print(t)
    # print(len(s))
    # print(len(t))
    # print(s[0])
    # print(t[0])
    # print(s[0] != t[0])
    # print(s[0] == t[0])
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
