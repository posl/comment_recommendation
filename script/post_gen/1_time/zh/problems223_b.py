Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if len(s) == 1:
        print(s)
        print(s)
        return
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 2

def min_max_string(s):
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
Suggestion 3

def problem223_b():
    s = input()
    if len(s) == 1:
        print(s)
        print(s)
        return
    min_s = s
    max_s = s
    for i in range(0,len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 4

def main():
    S = input()
    Smin = S
    Smax = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < Smin:
            Smin = S
        if S > Smax:
            Smax = S
    print(Smin)
    print(Smax)

=======
Suggestion 5

def get_min_max(s):
    min_str = s
    max_str = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_str:
            min_str = s
        if s > max_str:
            max_str = s
    return min_str, max_str

=======
Suggestion 6

def main():
    print("请输入字符串：")
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 7

def get_min_max_str(s):
    l = len(s)
    min_str = s
    max_str = s
    for i in range(l):
        tmp_str = s[i:] + s[:i]
        if tmp_str < min_str:
            min_str = tmp_str
        if tmp_str > max_str:
            max_str = tmp_str
    return min_str, max_str

=======
Suggestion 8

def main():
    s = input()
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 9

def get_min_max(s):
    min = s
    max = s
    for i in range(0, len(s)):
        s = s[1:] + s[0]
        if s < min:
            min = s
        elif s > max:
            max = s
    return min, max

=======
Suggestion 10

def main():
    s = input()
    s_len = len(s)
    s_min = s
    s_max = s
    for i in range(s_len):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)
