Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    for i in range(3):
        if s[i] == "1":
            s = s[:i] + "0" + s[i+1:]
        else:
            s = s[:i] + "0" + s[i+1:]
    if s[3] == "1":
        s = s[:3] + "0"
    print(s)

=======
Suggestion 2

def main():
    S = input()
    ans = ""
    for i in range(3):
        if S[i] == "1":
            ans += "1"
        else:
            ans += "0"
    if S[3] == "1":
        ans += "0"
    else:
        ans += "0"
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = ''
    for i in range(3):
        if s[i] == '1':
            ans += '1'
        else:
            ans += '0'
    if s[3] == '1':
        ans += '0'
    else:
        ans += '0'
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    for i in range(3):
        if S[i] == "1":
            print("0", end="")
        else:
            print("0", end="")
    if S[3] == "1":
        print("0")
    else:
        print("0")

=======
Suggestion 5

def main():
    S = input()
    ans = ''
    for i in range(4):
        if i == 3:
            ans += '0'
        else:
            ans += S[i+1]
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    ans = ""
    for i in range(0, len(s)):
        if i == len(s) - 1:
            break
        if s[i] == "1":
            ans += "1"
        else:
            ans += "0"
    if s[len(s) - 1] == "1":
        ans += "0"
    else:
        ans += "0"
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    print(S[1] + S[2] + S[3] + "0")

=======
Suggestion 8

def main():
    s = input()
    print(s[1], s[2], s[3], sep="")

=======
Suggestion 9

def main():
    s = input()
    print(s[1:] + "0")

=======
Suggestion 10

def main():
    s = input()
    print(s[:-1])
