Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r+l-2-i]
    return ''.join(s)

=======
Suggestion 2

def reverseString(s, l, r):
    l -= 1
    r -= 1
    temp = s[l:r+1]
    temp = temp[::-1]
    s = s[:l] + temp + s[r+1:]
    return s

=======
Suggestion 3

def reverse_string(string, start, end):
    string_list = list(string)
    string_list[start:end+1] = reversed(string_list[start:end+1])
    return "".join(string_list)

L, R = map(int, input().split())
S = input()
print(reverse_string(S, L-1, R-1))

=======
Suggestion 4

def reverse(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l+i-1], s[r-i-1] = s[r-i-1], s[l+i-1]
    return ''.join(s)

=======
Suggestion 5

def reverse_string(s, start, end):
    s[start:end+1] = list(reversed(s[start:end+1]))
    return s

=======
Suggestion 6

def reverse_string(s, L, R):
    s = s[:L-1] + s[L-1:R][::-1] + s[R:]
    return s

=======
Suggestion 7

def reverse_string(string, start, end):
    string_list = list(string)
    while start < end:
        temp = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = temp
        start += 1
        end -= 1
    return ''.join(string_list)

=======
Suggestion 8

def rev(s,start,end):
    return s[:start-1]+s[start-1:end][::-1]+s[end:]

=======
Suggestion 9

def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = reversed(s[l-1:r])
    return ''.join(s)

=======
Suggestion 10

def reverse(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]
