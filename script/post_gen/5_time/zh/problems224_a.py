Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[-2:] == "er":
        print("er")
    else:
        print("ist")

=======
Suggestion 2

def main():
    s = input()
    if s.endswith("er"):
        print("er")
    else:
        print("ist")

=======
Suggestion 3

def main():
    S = input()
    if S.endswith('er'):
        print('er')
    else:
        print('ist')

=======
Suggestion 4

def main():
    s = input()
    if s.endswith("er"):
        print("er")
    elif s.endswith("ist"):
        print("ist")
    else:
        print("error")

=======
Suggestion 5

def get_suffix(s):
    if s.endswith("er"):
        return "er"
    elif s.endswith("ist"):
        return "ist"
    else:
        return "error"

=======
Suggestion 6

def main():
    s = input()
    if s[-2:] == "er":
        print("er")
    elif s[-3:] == "ist":
        print("ist")

=======
Suggestion 7

def problem224_a():
    s = input()
    if s.endswith("er"):
        print("er")
    else:
        print("ist")
