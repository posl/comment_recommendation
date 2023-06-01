Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 2

def reverse_str(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l-1+i], s[r-1-i] = s[r-1-i], s[l-1+i]
    return ''.join(s)

=======
Suggestion 3

def reverse(s, L, R):
    s = list(s)
    if L == 1:
        return ''.join(list(reversed(s[L-1:R]))) + ''.join(s[R:])
    else:
        return ''.join(s[:L-1]) + ''.join(list(reversed(s[L-1:R]))) + ''.join(s[R:])

=======
Suggestion 4

def main():
    L,R = map(int,input().split())
    S = input()
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(S)

=======
Suggestion 5

def reverse_string(string, start, end):
    """Reverse string from start to end."""
    string = list(string)
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return ''.join(string)

=======
Suggestion 6

def main():
    L,R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 7

def reverse(s, l, r):
    return s[:l] + s[l:r+1][::-1] + s[r+1:]

l, r = map(int, input().split())
s = input()
print(reverse(s, l-1, r-1))

=======
Suggestion 8

def reverse_string(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 9

def reverseString(s, l, r):
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]
    return s

=======
Suggestion 10

def reverse(s, l, r):
    s = list(s)
    s[l-1:r] = reversed(s[l-1:r])
    return "".join(s)
