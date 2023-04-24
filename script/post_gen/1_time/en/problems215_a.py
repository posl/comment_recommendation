Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s == "Hello,World!":
        print("AC")
    else:
        print("WA")

=======
Suggestion 2

def main():
    s = input()
    if s == 'Hello,World!':
        print('AC')
    else:
        print('WA')

=======
Suggestion 3

def main():
    S = input()
    if S == "Hello,World!":
        print("AC")
    else:
        print("WA")

=======
Suggestion 4

def main():
    input_string = input()
    if input_string == "Hello,World!":
        print("AC")
    else:
        print("WA")

=======
Suggestion 5

def isMatch(s):
    if len(s) != 12:
        return False
    if s[0:5] != "Hello":
        return False
    if s[5:6] != ",":
        return False
    if s[6:12] != "World!":
        return False
    return True

=======
Suggestion 6

def main():
    input_str = input()
    if input_str == "Hello,World!":
        print("AC")
    else:
        print("WA")
