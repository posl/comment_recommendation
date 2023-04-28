Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 2

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 3

def reverse_string(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

l, r = map(int, input().split())
s = input()
print(reverse_string(s, l, r))

=======
Suggestion 4

def reverse(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 5

def reverse_str(s, l, r):
    if l == 1:
        return s[r-1::-1] + s[r:]
    else:
        return s[:l-1] + s[r-1:l-2:-1] + s[r:]

l, r = map(int, input().split())
s = input()

print(reverse_str(s, l, r))

=======
Suggestion 6

def reverse_string(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 7

def reverse_string(string, start, end):
    string = string[:start-1] + string[start-1:end][::-1] + string[end:]
    return string

L, R = map(int, input().split())
S = input()

print(reverse_string(S, L, R))

=======
Suggestion 8

def reverse_string(s, start, end):
    left = s[:start-1]
    middle = s[start-1:end]
    right = s[end:]
    middle = middle[::-1]
    return left + middle + right
