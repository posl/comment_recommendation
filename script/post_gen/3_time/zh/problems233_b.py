Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 2

def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    return ''.join(s)

=======
Suggestion 3

def reverse(s, l, r):
    return s[:l - 1] + s[l - 1:r][::-1] + s[r:]

=======
Suggestion 4

def reverse(s, L, R):
    return s[:L-1] + s[L-1:R][::-1] + s[R:]

=======
Suggestion 5

def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    s = ''.join(s)
    return s

=======
Suggestion 6

def reverse_str(s, l, r):
    if l < 1 or r > len(s):
        return s
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 7

def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r-1+l-i-1]
    return ''.join(s)

=======
Suggestion 8

def reverse_string(string, l, r):
    return string[:l-1] + string[l-1:r][::-1] + string[r:]
