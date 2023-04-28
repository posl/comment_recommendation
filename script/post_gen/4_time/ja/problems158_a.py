Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.count("A") == 1 and s.count("B") == 2:
        print("Yes")
    elif s.count("A") == 2 and s.count("B") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print('Yes')
    elif s.count('B') == 1 and s.count('A') == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if s.count("A") == 1 and s.count("B") == 2:
        print("Yes")
    elif s.count("B") == 1 and s.count("A") == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    if S.count("A") == 1 and S.count("B") == 2:
        print("Yes")
    elif S.count("B") == 1 and S.count("A") == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = list(input())
    if s.count("A") == 1 and s.count("B") == 2:
        print("Yes")
    elif s.count("A") == 2 and s.count("B") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    if S[0] != S[1] and S[0] != S[2] and S[1] != S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    if s.count('A') == 1 or s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    S = input()
    if S == "AAA" or S == "BBB":
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def main():
    s = input()
    print("Yes") if s.count("A") == 1 or s.count("B") == 1 else print("No")
