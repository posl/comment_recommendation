Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    input_str = input()
    if input_str == "AAA" or input_str == "BBB":
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print('Yes')
    elif s.count('A') == 2 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print('No')
    else:
        print('Yes')
