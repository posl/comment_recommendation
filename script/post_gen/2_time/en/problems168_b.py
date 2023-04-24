Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + "...")

=======
Suggestion 2

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')

=======
Suggestion 3

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")

main()
