Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse_string(s, l, r):
    # 1. 从s中取出l至r的子串
    substr = s[l-1:r]
    # 2. 将子串反转
    substr = substr[::-1]
    # 3. 将反转后的子串替换到原串中
    s = s[:l-1] + substr + s[r:]
    print(s)

=======
Suggestion 2

def reverse_string(s, l, r):
    s_list = list(s)
    s_list[l-1:r] = s_list[l-1:r][::-1]
    return ''.join(s_list)

=======
Suggestion 3

def reverse_string(s, l, r):
    if l > r:
        return s
    else:
        s = s[:l-1] + s[r-1:l-2:-1] + s[r:]
        return s

=======
Suggestion 4

def reverse(s, start, end):
    s = list(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    s = ''.join(s)
    return s

=======
Suggestion 5

def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    return ''.join(s)

=======
Suggestion 6

def problems233_b():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 7

def reverse_string(string, start, end):
    return string[:start] + string[start:end+1][::-1] + string[end+1:]

=======
Suggestion 8

def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r - i + l - 2]
    return ''.join(s)

=======
Suggestion 9

def reverse_string(l,r,s):
    s1 = s[:l-1]
    s2 = s[l-1:r]
    s3 = s[r:]
    s2 = s2[::-1]
    return s1+s2+s3

=======
Suggestion 10

def reverse_string(string, begin, end):
    return string[:begin] + string[begin:end+1][::-1] + string[end+1:]
