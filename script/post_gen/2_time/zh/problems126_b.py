Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 2

def problems126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1]+s[k-1].lower()+s[k:])
problems126_a()

=======
Suggestion 3

def problem126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 4

def problems126_a():
    N, K = map(int, input().split())
    S = input()
    S1 = S[K-1]
    S2 = S1.lower()
    S3 = S[:K-1] + S2 + S[K:]
    print(S3)

=======
Suggestion 5

def problems126_a():
    N,K = map(int,input().split())
    S = input()
    print(S[:K-1]+S[K-1].lower()+S[K:])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])
