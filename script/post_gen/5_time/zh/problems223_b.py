Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        elif s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 2

def main():
    s = input()
    min = s
    max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s > max:
            max = s
        if s < min:
            min = s
    print(min)
    print(max)

=======
Suggestion 3

def min_max(S):
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    return S_min, S_max

=======
Suggestion 4

def main():
    s = input()
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:]+s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 5

def minmax(S):
    min_str = S
    max_str = S
    for i in range(1, len(S)):
        S = S[1:] + S[0]
        if S < min_str:
            min_str = S
        if S > max_str:
            max_str = S
    return min_str, max_str

=======
Suggestion 6

def min_max(s):
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    return min_s, max_s

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    # 1. 左移，右移
    # 2. 左移，左移
    # 3. 右移，右移
    # 4. 右移，左移
    # 5. 左移，右移，左移
    # 6. 左移，左移，右移
    # 7. 右移，左移，右移
    # 8. 右移，右移，左移
    # 9. 左移，右移，左移，右移
    # 10. 左移，左移，右移，左移
    # 11. 右移，左移，右移，左移
    # 12. 右移，右移，左移，右移
    # 13. 左移，右移，左移，右移，左移
    # 14. 左移，左移，右移，左移，右移
    # 15. 右移，左移，右移，左移，右移
    # 16. 右移，右移，左移，右移，左移
    # 17. 左移，右移，左移，右移，左移，右移
    # 18. 左移，左移，右移，左移，右移，左移
    # 19. 右移，左移，右移，左移，右移，左移
    # 20. 右移，右移，左移，右移，左移，右移
    # 21. 左移，右移，左移，右移，左移，右移，左移
    # 22. 左移，左移，右移，左移，右移，左移，右移
    # 23. 右移，左移，右移，左移，右移，左移，右移
    # 24. 右移，右移，左移，右移，左移，右移，左移
    # 25. 左移，右移，左移，右移，左

=======
Suggestion 8

def main():
    s = input()
    t = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < t:
            t = s
    print(t)
    s = t
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s > t:
            t = s
    print(t)

=======
Suggestion 9

def get_min_max(s):
    s_list = list(s)
    min_s = s
    max_s = s
    for i in range(len(s)):
        s_list.append(s_list[0])
        s_list.remove(s_list[0])
        str_tmp = ''.join(s_list)
        if str_tmp < min_s:
            min_s = str_tmp
        if str_tmp > max_s:
            max_s = str_tmp
    return min_s, max_s
