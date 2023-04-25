Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = list(input())
    S[K-1] = S[K-1].lower()
    print(''.join(S))

=======
Suggestion 4

def problem126_a():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

problem126_a()

=======
Suggestion 5

def lower_case(s, k):
    return s[:k-1] + s[k-1].lower() + s[k:]

=======
Suggestion 6

def lower_case_kth_char(S, K):
    return S[:K-1] + S[K-1].lower() + S[K:]
