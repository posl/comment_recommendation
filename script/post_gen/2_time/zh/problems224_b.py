Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[-2:] == "er":
        print("er")
    elif S[-3:] == "ist":
        print("ist")
    else:
        print("er")

=======
Suggestion 2

def main():
    s = input()
    if s[-2:] == "er":
        print("er")
    else:
        print("ist")

=======
Suggestion 3

def main():
    S = input()
    if S[-2:] == "er":
        print("er")
    else:
        print("ist")

=======
Suggestion 4

def main():
    S = input()
    if S.endswith("er"):
        print("er")
    elif S.endswith("ist"):
        print("ist")

=======
Suggestion 5

def main():
    s = input()
    if s[-2:] == 'er':
        print('er')
    else:
        print('ist')

=======
Suggestion 6

def solution(s):
    if s.endswith("er"):
        print("er")
    elif s.endswith("ist"):
        print("ist")
    else:
        print("")
