Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s[1] + s[2] + s[0])

=======
Suggestion 2

def main():
    S = input()
    print(S[1] + S[2] + S[0])

=======
Suggestion 3

def main():
    s = input()
    print(s[1:] + s[0])

=======
Suggestion 4

def main():
    S = input()
    print(S[1:] + S[0])

=======
Suggestion 5

def main():
    s = list(input())
    s.append(s.pop(0))
    print("".join(s))
