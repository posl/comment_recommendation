Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    S = input()
    S = S[:K-1] + S[K-1].lower() + S[K:]
    print(S)

=======
Suggestion 2

def problems126_a():
    n, k = map(int, input().split())
    s = input()
    print(s[0:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 4

def underline():
    n,k=input().split()
    n=int(n)
    k=int(k)
    s=input()
    s=list(s)
    s[k-1]=s[k-1].lower()
    s=''.join(s)
    print(s)
underline()

=======
Suggestion 5

def main():
    N,K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    s = input()
    s = s[:k-1] + s[k-1].lower() + s[k:]
    print(s)

=======
Suggestion 7

def problems126_a():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])
