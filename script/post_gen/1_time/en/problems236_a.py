Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

s = input()
a, b = map(int, input().split())

print(swap(s, a, b))

=======
Suggestion 2

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 3

def swap(S, a, b):
    return S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]

S = input()
a, b = map(int, input().split())
print(swap(S, a, b))

=======
Suggestion 4

def solve():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 5

def swap():
    s = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    s = ''.join(s)
    print(s)

swap()

=======
Suggestion 6

def swap_char(s, a, b):
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    return ''.join(s)

=======
Suggestion 7

def swap(s, a, b):
    a-=1
    b-=1
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

=======
Suggestion 8

def swap(a,b,word):
    a = a - 1
    b = b - 1
    word[a], word[b] = word[b], word[a]
    return word
