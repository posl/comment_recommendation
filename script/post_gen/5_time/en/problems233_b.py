Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 2

def reverse_string(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 3

def reverseString(s, start, end):
    s = list(s)
    while(start < end):
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

=======
Suggestion 4

def reverse_string(string, start, stop):
    if start == 0:
        return string[stop::-1] + string[stop+1:]
    else:
        return string[:start-1] + string[stop:start-2:-1] + string[stop+1:]

=======
Suggestion 5

def reverse_string(string, start, end):
    return string[:start-1] + string[start-1:end][::-1] + string[end:]

=======
Suggestion 6

def reverse_string(string, start, end):
    string = string[:start-1] + string[start-1:end][::-1] + string[end:]
    return string

=======
Suggestion 7

def reverse_string(string, start, end):
    string = list(string)
    string[start-1:end] = reversed(string[start-1:end])
    return ''.join(string)

=======
Suggestion 8

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

=======
Suggestion 9

def reverse_string(string, start, end):
    return string[:start] + string[start:end][::-1] + string[end:]

=======
Suggestion 10

def reverseStr(s):
    return s[::-1]
