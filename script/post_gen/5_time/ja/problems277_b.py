Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    if len(s) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def check_str(s):
    #print(s)
    if s[0] in ['H','D','C','S'] and s[1] in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        return True
    else:
        return False

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    if len(s) == len(set(s)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    if len(set(S)) == len(S):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    #print(len(S))
    #print(len(set(S)))
    #print(set(S))
    if N == len(set(S)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print("Yes" if n == len(s) else "No")
