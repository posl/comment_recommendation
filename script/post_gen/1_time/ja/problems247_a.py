Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    for i in range(3):
        if S[i] == "1":
            S = S[:i] + "0" + S[i+1:]
        else:
            S = S[:i] + "0" + S[i+1:]
    print(S)

=======
Suggestion 2

def main():
    S = input()
    ans = ""
    for i in range(len(S)):
        if i == len(S) - 1:
            ans += "0"
        else:
            ans += S[i + 1]
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    for i in range(len(S)):
        if i == len(S) - 1:
            print("0")
        elif S[i] == "1":
            print("1", end="")
        else:
            print("0", end="")

=======
Suggestion 4

def main():
    S = input()
    S = S.replace("1","2")
    S = S.replace("0","1")
    S = S.replace("2","0")
    print(S)

=======
Suggestion 5

def main():
    s = input()
    ans = ''
    for i in range(len(s)-1):
        ans += s[i+1]
    ans += '0'
    print(ans)

=======
Suggestion 6

def move(S):
    ans = ''
    for i in range(len(S)-1):
        ans += S[i+1]
    ans += '0'
    return ans

S = input()
print(move(S))

=======
Suggestion 7

def main():
    S = input()
    for i in range(0, len(S)-1):
        print(S[i], end='')
    print(S[len(S)-1])

=======
Suggestion 8

def main():
    S = input()
    S = S.replace("1","1 ")
    S = S.replace("0","0 ")
    S = S.split()
    S = S[0:-1]
    S = " ".join(S)
    print(S)

=======
Suggestion 9

def main():
    s = input()
    s = s[1:] + "0"
    print(s)

=======
Suggestion 10

def main():
    S = input()
    print(S[1:] + "0")
