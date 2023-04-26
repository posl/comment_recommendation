Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 2

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 3

def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = s[l-1:r][::-1]
    print(''.join(s))

=======
Suggestion 4

def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = s[l-1:r][::-1]
    print("".join(s))

=======
Suggestion 5

def Main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])
