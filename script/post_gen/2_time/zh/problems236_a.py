Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(s,a,b):
    s1 = s[:a-1]
    s2 = s[a-1]
    s3 = s[a:b-1]
    s4 = s[b-1]
    s5 = s[b:]
    return s1 + s4 + s3 + s2 + s5

=======
Suggestion 2

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 3

def swap(s,a,b):
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    return "".join(s)

=======
Suggestion 4

def swap(s, a, b):
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    return ''.join(s)

=======
Suggestion 5

def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print(''.join(S))

=======
Suggestion 6

def main():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 7

def swap_char(s, a, b):
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 8

def main():
    s = input()
    a, b = map(int, input().split())
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    print(''.join(s))

=======
Suggestion 9

def problem236_a():
    S = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

=======
Suggestion 10

def main():
    s = input()
    a,b = map(int, input().split())
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    print(''.join(s))
main()
