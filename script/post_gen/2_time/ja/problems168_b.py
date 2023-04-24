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
    if len(S) > K:
        print(S[:K] + '...')
    else:
        print(S)

=======
Suggestion 4

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

=======
Suggestion 5

def main():
    K = int(input())
    S = str(input())
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)

=======
Suggestion 6

def main():
    k = int(input())
    s = input()
    n = len(s)
    if k >= n:
        print(s)
    else:
        print(s[:k] + "...")

=======
Suggestion 7

def main():
    #入力
    K = int(input())
    S = input()
    #Sの長さがKを上回っているならば、先頭K文字だけを切り出し、末尾に...を付加して出力
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")

=======
Suggestion 8

def main():
    #K
    K = int(input())
    #S
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")
