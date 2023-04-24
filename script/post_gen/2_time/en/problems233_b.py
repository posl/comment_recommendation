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
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = reversed(S[L-1:R])
    print(''.join(S))

=======
Suggestion 4

def reverse_string(L, R, S):
    return S[:L-1] + S[L-1:R][::-1] + S[R:]

L, R = map(int, input().split())
S = input()
print(reverse_string(L, R, S))

=======
Suggestion 5

def reverse_string(string, left, right):
    return string[:left-1] + string[left-1:right][::-1] + string[right:]
