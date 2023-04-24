Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count('For') > s.count('Against'):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("Yes" if s.count("For") > s.count("Against") else "No")

=======
Suggestion 3

def main():
    n = int(input())
    a = [input() for i in range(n)]
    if a.count("For") > a.count("Against"):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n = int(input())
    for_count = 0
    against_count = 0
    for i in range(n):
        s = input()
        if s == "For":
            for_count += 1
        else:
            against_count += 1
    if for_count > against_count:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if s.count("For") > n//2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    S_list = []
    for i in range(N):
        S_list.append(input())
    if S_list.count("For") > N/2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(n):
        s = input()
        if s == "For":
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def check_majority():
    N = int(input())
    if N%2 != 0:
        S = []
        for i in range(N):
            S.append(input())
        if S.count('For') > S.count('Against'):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
