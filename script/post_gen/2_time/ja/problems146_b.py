Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = ""
    for s in S:
        ans += chr((ord(s) - ord('A') + N) % 26 + ord('A'))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        if ord(i) + n > ord("Z"):
            ans += chr(ord(i) + n - ord("Z") + ord("A") - 1)
        else:
            ans += chr(ord(i) + n)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = ""
    for c in S:
        ans += chr((ord(c)-ord('A')+N)%26+ord('A'))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = ""
    for s in S:
        ans += chr((ord(s)-65+N)%26+65)
    print(ans)

=======
Suggestion 5

def main():
    N=int(input())
    S=input()
    for i in S:
        if ord(i)+N>ord("Z"):
            print(chr(ord(i)+N-26),end="")
        else:
            print(chr(ord(i)+N),end="")

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = ""

    for i in range(len(S)):
        if S[i] == "Z":
            ans += "A"
        else:
            ans += chr(ord(S[i])+N)

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = ''
    for i in S:
        ans += chr((ord(i)-65+N)%26+65)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        if ord(s[i])+n > 90:
            ans += chr((ord(s[i])+n)-26)
        else:
            ans += chr(ord(s[i])+n)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    for i in S:
        #print(i)
        if ord(i)+N > 90:
            print(chr(ord(i)+N-26),end="")
        else:
            print(chr(ord(i)+N),end="")

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    def change(S):
        return chr((ord(S) - ord('A') + N) % 26 + ord('A'))
    print("".join(map(change, S)))
