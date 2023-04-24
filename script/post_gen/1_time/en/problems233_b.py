Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

main()

=======
Suggestion 2

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 3

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print(''.join(S))

=======
Suggestion 4

def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = s[l-1:r][::-1]
    print(''.join(s))

=======
Suggestion 5

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L - 1:R] = S[L - 1:R][::-1]
    print("".join(S))

=======
Suggestion 6

def reverse(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 7

def reverse(l, r, s):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 8

def reverseString(s, l, r):
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]
    return s

=======
Suggestion 9

def reverse_string(string, l, r):
    return string[:l-1] + string[l-1:r][::-1] + string[r:]
