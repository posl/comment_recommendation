Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = ""
    for i in range(4):
        if i == 3:
            ans += "0"
        else:
            ans += s[i]
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    print(s[1] + s[2] + s[3] + '0')

=======
Suggestion 3

def main():
    S = input()
    ans = ""
    for i in range(0, len(S)-1):
        ans += S[i]
    ans += "0"
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    S = S[0:3]
    S = '0' + S
    print(S)

=======
Suggestion 5

def main():
    S = input()
    S = S[0:3]
    S = "0" + S
    print(S)

=======
Suggestion 6

def main():
    s = input()
    for i in range(len(s)-1):
        print(s[i],end="")
    print("0")

=======
Suggestion 7

def main():
    S = input()
    #print(S)
    result = ''
    for i in range(0,4):
        if i == 3:
            result = result + '0'
        else:
            result = result + S[i]
    print(result)

=======
Suggestion 8

def main():
    s = input()
    print(s[1:] + '0')

=======
Suggestion 9

def main():
    S = input()
    print(S[1:4] + '0')

=======
Suggestion 10

def main():
    s = input()
    print(s[1:] + "0")
