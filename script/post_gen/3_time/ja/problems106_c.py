Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    cnt = 0
    for i in range(len(s)):
        if s[i] == "1":
            cnt += 1
        else:
            break
    if k <= cnt:
        print(1)
    else:
        print(s[cnt])

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != "1":
            print(s[i])
            break
    else:
        print(1)

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
    else:
        for i in range(len(s)):
            if s[i] != '1':
                print(s[i])
                break

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    l = len(s)
    i = 0
    while i < l:
        if s[i] == '1':
            i += 1
        else:
            break
    if k <= i:
        print(1)
    else:
        print(s[i])

=======
Suggestion 5

def get_digit(num):
    digit = 0
    while num > 0:
        num //= 10
        digit += 1
    return digit

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    l = len(S)
    for i in range(l):
        if S[i] != '1':
            print(S[i])
            break
        elif i == l-1:
            print(1)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    #print(S,K)
    cnt = 0
    for i in range(len(S)):
        if S[i] == "1":
            cnt += 1
        else:
            break
    if cnt >= K:
        print(1)
    else:
        print(S[cnt])

=======
Suggestion 8

def main():
    s = input()
    k = int(input())

    def f(s):
        t = ""
        for c in s:
            if c != "1":
                t += c * int(c)
            else:
                t += c
        return t

    for _ in range(k):
        s = f(s)

    print(s[k - 1])

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    print(s[(k-1)//len(s)])

=======
Suggestion 10

def main():
    str = input()
    num = int(input())
    if num <= len(str):
        print(str[num-1])
    else:
        for i in range(0, num-len(str)):
            str = str.replace("2", "22")
            str = str.replace("3", "333")
            str = str.replace("4", "4444")
            str = str.replace("5", "55555")
            str = str.replace("6", "666666")
            str = str.replace("7", "7777777")
            str = str.replace("8", "88888888")
            str = str.replace("9", "999999999")
        print(str[num-1])
