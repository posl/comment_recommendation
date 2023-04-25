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
    L, R = map(int, input().split())
    S = input()
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(S)

=======
Suggestion 3

def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = reversed(S[L-1:R])
    print(''.join(S))

=======
Suggestion 4

def solve():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 5

def reverse_string(L,R,S):
    return S[0:L-1] + S[L-1:R][::-1] + S[R:]

L,R = map(int,input().split())
S = input()
print(reverse_string(L,R,S))

=======
Suggestion 6

def main():
    # Read the input
    L, R = map(int, input().split())
    S = input()
    # Reverse the substring
    S = S[:L - 1] + S[L - 1:R][::-1] + S[R:]
    # Print the result
    print(S)
