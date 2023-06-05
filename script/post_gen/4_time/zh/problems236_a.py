Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = raw_input()
    a,b = map(int,raw_input().split())
    print s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:]

=======
Suggestion 2

def swap(a, b, s):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 3

def main():
    S = input()
    a, b = map(int, input().split())
    print(S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:])

=======
Suggestion 4

def swap(s, a, b):
    s1 = s[:a-1]
    s2 = s[a-1]
    s3 = s[a:b-1]
    s4 = s[b-1]
    s5 = s[b:]
    return s1+s4+s3+s2+s5

=======
Suggestion 5

def main():
    s = input()
    a, b = map(int, input().split())
    print(s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])

=======
Suggestion 6

def swapchar(s,a,b):
    a = a - 1
    b = b - 1
    t = s[a]
    s[a] = s[b]
    s[b] = t
    return s

=======
Suggestion 7

def swap(s, a, b):
    a = a - 1
    b = b - 1
    s = list(s)
    tmp = s[a]
    s[a] = s[b]
    s[b] = tmp
    return ''.join(s)

=======
Suggestion 8

def problem236_a():
    s = input()
    a,b = map(int, input().split())

    lst = list(s)
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
    print(''.join(lst))

=======
Suggestion 9

def swap(s, a, b):
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    return "".join(s)

S = input()
a, b = map(int, input().split())
print(swap(S, a, b))
