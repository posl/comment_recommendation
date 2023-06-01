Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    print(''.join(s))

=======
Suggestion 2

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 3

def my_swap(s, a, b):
    if a > b:
        a, b = b, a
    if a == b:
        return s
    if a == 1:
        return s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 4

def swap(a, b, s):
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    return ''.join(s)

=======
Suggestion 5

def main():
    S = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

=======
Suggestion 6

def main():
    s = raw_input()
    a, b = map(int, raw_input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print s

=======
Suggestion 7

def swap(a, b, s):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 8

def swap_char(s, a, b):
    a = a - 1
    b = b - 1
    s[a], s[b] = s[b], s[a]
    return s

=======
Suggestion 9

def swap(s, a, b):
    a = a - 1
    b = b - 1
    s[a], s[b] = s[b], s[a]
    return s
