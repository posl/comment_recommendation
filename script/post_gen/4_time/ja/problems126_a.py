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
    n, k = map(int, input().split())
    s = input()
    print(s[0:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    S = input()
    S = S[:K-1] + S[K-1].lower() + S[K:]
    print(S)
