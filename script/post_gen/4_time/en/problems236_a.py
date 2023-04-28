Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 2

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 3

def main():
    S = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

=======
Suggestion 4

def swap(a, b, s):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 5

def main():
    S = input()
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(S[:a] + S[b] + S[a + 1:b] + S[a] + S[b + 1:])

=======
Suggestion 6

def swap_char(s, a, b):
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    return ''.join(s)

=======
Suggestion 7

def swap():
    S = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

=======
Suggestion 8

def swap(s, a, b):
    s = list(s)
    a = a - 1
    b = b - 1
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

=======
Suggestion 9

def swap_char(str, a, b):
    a = a - 1
    b = b - 1
    str = list(str)
    str[a], str[b] = str[b], str[a]
    return ''.join(str)

str = input()
a, b = map(int, input().split())
print(swap_char(str, a, b))

=======
Suggestion 10

def swap(string, a, b):
    string = list(string)
    string[a-1], string[b-1] = string[b-1], string[a-1]

    return ''.join(string)
