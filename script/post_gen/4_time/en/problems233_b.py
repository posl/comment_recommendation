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
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 4

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print(''.join(S))

=======
Suggestion 5

def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = reversed(s[l-1:r])
    print(''.join(s))

=======
Suggestion 6

def reverse_string(L, R, S):
    return S[:L-1] + S[L-1:R][::-1] + S[R:]

=======
Suggestion 7

def reverse_string(start, end, string):
    return string[:start] + string[start:end+1][::-1] + string[end+1:]
