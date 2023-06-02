Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    str = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    str = list(str)
    str[a], str[b] = str[b], str[a]
    for i in str:
        print(i, end='')

=======
Suggestion 2

def swap(s, a, b):
    a -= 1
    b -= 1
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

=======
Suggestion 3

def main():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 4

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 5

def swap(s,a,b):
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    return ''.join(s)

=======
Suggestion 6

def main():
    S = input()
    a, b = map(int, input().split())
    print(S[:a - 1] + S[b - 1] + S[a:b - 1] + S[a - 1] + S[b:])

=======
Suggestion 7

def swap(s, a, b):
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 8

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

=======
Suggestion 9

def main():
    S = input()
    a, b = map(int, input().split())
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    print(S)
