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
    S = input()
    S = S[:K-1] + S[K-1].lower() + S[K:]
    print(S)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = S[:K-1] + S[K-1].lower() + S[K:]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S[K-1] = S[K-1].lower()
    S = ''.join(S)
    print(S)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    s = input()
    s = s[:k-1] + s[k-1].lower() + s[k:]
    print(s)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K - 1] + S[K - 1].lower() + S[K:])
    return
