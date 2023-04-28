Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count("For") > n/2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count('For') > n/2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count("For") > n//2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if s.count("For") > n//2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    if s.count('For') > n//2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] == 'For':
            S[i] = 1
        else:
            S[i] = 0
    if sum(S) > N/2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("Yes" if s.count("For") > n//2 else "No")

=======
Suggestion 8

def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s = input()
        s_list.append(s)

    if s_list.count('For') > n//2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print('Yes' if s.count('For') > n / 2 else 'No')

=======
Suggestion 10

def judge():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        if s[i] == 'For':
            s[i] = 1
        else:
            s[i] = 0
    if sum(s) > n//2:
        print('Yes')
    else:
        print('No')

judge()
