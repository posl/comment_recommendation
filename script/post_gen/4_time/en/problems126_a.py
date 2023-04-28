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
    n, k = map(int, input().split())
    s = input()
    s = s[:k-1] + s[k-1].lower() + s[k:]
    print(s)

main()

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    s = list(input())
    s[k-1] = s[k-1].lower()
    print("".join(s))

=======
Suggestion 5

def main():
    # input
    N, K = map(int, input().split())
    S = input()

    # output
    print(S[:K-1]+S[K-1].lower()+S[K:])

=======
Suggestion 6

def main():
    # Read the input
    n, k = map(int, input().split())
    s = input()
    # Print the output
    print(s[:k-1] + s[k-1].lower() + s[k:])

main()
