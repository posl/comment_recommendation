Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = list(input())
    if S[0] == "1":
        print("1", end="")
    else:
        print("0", end="")
    if S[1] == "1":
        print("1", end="")
    else:
        print("0", end="")
    if S[2] == "1":
        print("1", end="")
    else:
        print("0", end="")
    if S[3] == "1":
        print("1")
    else:
        print("0")

=======
Suggestion 2

def main():
    s = input()
    s = s.replace('1', '2')
    s = s.replace('0', '1')
    s = s.replace('2', '0')
    print(s)

=======
Suggestion 3

def main():
    S = input()
    print(S[1:]+"0" if S[0] == "1" else S[1:]+"1")

=======
Suggestion 4

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 5

def main():
    S = input()
    print(S[1:] + S[0])

=======
Suggestion 6

def main():
    s = input()
    print(s[1:4]+s[0])
