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
    N, K = map(int, input().split())
    S = list(input())
    S[K-1] = S[K-1].lower()
    print("".join(S))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    K = K - 1
    print(S[:K] + S[K].lower() + S[K+1:])
