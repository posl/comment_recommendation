Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S + S
    S_min = S[0]
    S_max = S[0]
    for i in range(1,len(S)//2):
        if S[i:] < S_min:
            S_min = S[i:]
        if S[i:] > S_max:
            S_max = S[i:]
    print(S_min)
    print(S_max)

=======
Suggestion 2

def shift(s, n):
    return s[n:] + s[:n]

=======
Suggestion 3

def main():
    s = input()
    s = s * 2
    length = len(s)
    min_s = s[:length//2]
    max_s = s[:length//2]
    for i in range(1, length//2):
        if min_s > s[i:i+length//2]:
            min_s = s[i:i+length//2]
        if max_s < s[i:i+length//2]:
            max_s = s[i:i+length//2]
    print(min_s)
    print(max_s)

=======
Suggestion 4

def get_min_max(s):
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
Suggestion 5

def main():
    S = input()
    S = S * 2
    S_min = S[0:len(S)//2]
    S_max = S[0:len(S)//2]
    for i in range(1, len(S)//2):
        S_tmp = S[i:i+len(S)//2]
        if S_tmp < S_min:
            S_min = S_tmp
        if S_tmp > S_max:
            S_max = S_tmp
    print(S_min)
    print(S_max)

=======
Suggestion 6

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
Suggestion 7

def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        s_min = min(s, s_min)
        s_max = max(s, s_max)
    print(s_min)
    print(s_max)

=======
Suggestion 8

def min_max_str(str):
    str_list = list(str)
    min_str = str
    max_str = str
    for i in range(len(str)):
        str_list.append(str_list.pop(0))
        str_temp = ''.join(str_list)
        if str_temp < min_str:
            min_str = str_temp
        if str_temp > max_str:
            max_str = str_temp
    return min_str, max_str

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    s = s+s
    min_s = s[:n]
    max_s = s[:n]
    for i in range(1,n):
        if s[i:i+n] < min_s:
            min_s = s[i:i+n]
        if s[i:i+n] > max_s:
            max_s = s[i:i+n]
    print(min_s)
    print(max_s)

=======
Suggestion 10

def find_min_max(s):
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    return min_s, max_s
