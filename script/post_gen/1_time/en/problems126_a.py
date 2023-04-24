Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    S = S[:K-1] + S[K-1].lower() + S[K:]
    print(S)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])
main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    if K == 1:
        print(S[0].lower() + S[1:])
    else:
        print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 6

def main():
    # Write your code here
    n, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 7

def lowerCaseKthCharacter(N, K, S):
    if K > N:
        return "K should be less than N"
    else:
        return S[:K-1] + S[K-1].lower() + S[K:]
