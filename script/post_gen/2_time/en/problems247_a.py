Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    print(s[1] + s[2] + s[3] + '0')

=======
Suggestion 2

def main():
    S = input()
    print(S[1] + S[2] + S[3] + '0')

main()

=======
Suggestion 3

def move(S):
    ans = ""
    for i in range(len(S)-1):
        ans += S[i]
    ans += "0"
    return ans

S = input()
print(move(S))

=======
Suggestion 4

def main():
    S = input()
    print(S[1]+S[2]+S[3]+'0')

=======
Suggestion 5

def main():
    s = input()
    ans = ""
    for i in range(len(s)-1):
        ans += str(int(s[i] == "1"))
    ans += "0"
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    for i in range(0, len(s) - 1):
        print(s[i], end = '')
    print('0')

=======
Suggestion 7

def main():
    s = input()
    for i in range(len(s)-1):
        print(s[i], end='')
    print(0)

=======
Suggestion 8

def main():
    s = input()
    print(s[1:] + '0')

main()

=======
Suggestion 9

def main():
    s = input()
    print(s[1:4] + '0')

=======
Suggestion 10

def main():
    s = input()
    print(s[1:] + "0")
