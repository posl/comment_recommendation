Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    for i in range(0,3):
        if S[i] == '1':
            print('0',end='')
        else:
            print('0',end='')
    if S[3] == '1':
        print('0')
    else:
        print('0')

=======
Suggestion 2

def main():
    S = input()
    ans = ""
    for i in range(4):
        if S[i] == "1":
            ans = ans + "0"
        else:
            ans = ans + S[i]
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    print(S[1] + S[2] + S[3] + '0')

=======
Suggestion 4

def main():
    S = input()
    print(S[1] + S[2] + S[3] + "0")

=======
Suggestion 5

def main():
    s = input()
    ans = ''
    for i in range(3):
        ans += str(int(s[i]))
    ans += '0'
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    ans = ""
    for i in range(3):
        ans += str(int(S[i]))
    ans += "0"
    print(ans)

main()

=======
Suggestion 7

def main():
    s = input()
    print(s[1]+s[2]+s[3]+'0')

=======
Suggestion 8

def main():
    S = input()
    S = S[0:3]
    S = '0' + S
    print(S)

main()

=======
Suggestion 9

def main():
    S = input()
    print(S[1:] + "0")
