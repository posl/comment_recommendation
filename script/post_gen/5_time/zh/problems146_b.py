Synthesizing 10/10 solutions

=======
Suggestion 1

def moveN(n, s):
    res = ""
    for i in range(len(s)):
        t = ord(s[i]) + n
        if t > ord('Z'):
            t = t - ord('Z') + ord('A') - 1
        res = res + chr(t)
    print(res)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    N = N % 26
    for i in range(len(S)):
        if ord(S[i]) + N > ord('Z'):
            print(chr(ord(S[i]) + N - 26), end='')
        else:
            print(chr(ord(S[i]) + N), end='')

=======
Suggestion 3

def problem146_b():
    n = int(input())
    s = input()
    result = ''
    for i in range(len(s)):
        result += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(result)

=======
Suggestion 4

def move_str(s, n):
    if n == 0:
        return s
    else:
        res = ''
        for i in range(len(s)):
            tmp = ord(s[i]) + n
            if tmp > 90:
                tmp = tmp - 26
            res = res + chr(tmp)
        return res

=======
Suggestion 5

def moveN(string, n):
    result = ""
    for i in string:
        #print(ord(i))
        if (ord(i) + n) > 90:
            result += chr(ord(i) + n - 26)
        else:
            result += chr(ord(i) + n)
    return result

=======
Suggestion 6

def move_char(char, n):
    if ord(char) + n > ord('Z'):
        return chr(ord(char) + n - ord('Z') + ord('A') - 1)
    else:
        return chr(ord(char) + n)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    str = ''
    for i in s:
        if ord(i)+n > ord('Z'):
            str = str + chr(ord(i)+n-ord('Z')+ord('A')-1)
        else:
            str = str + chr(ord(i)+n)
    print(str)

=======
Suggestion 8

def problems146_b():
    # N = int(input())
    # S = input()

    N = 13
    S = "abcdefghijklmnopqrstuvwxyz"

    # N = 2
    # S = "ABCXYZ"

    # N = 0
    # S = "ABCXYZ"

    # N = 0
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 26
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 26
    # S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # N = 25
    # S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # N = 0
    # S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # N = 1
    # S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # N = 1
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 2
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 3
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 4
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 5
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 6
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 7
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 8
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 9
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 10
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 11
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 12
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 13
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 14
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 15
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 16
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 17
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 18
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 19
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 20
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 21
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 22
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 23
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 24
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 25
    # S = "abcdefghijklmnopqrstuvwxyz"

    # N = 26

=======
Suggestion 9

def move_char(c, n):
    if c.isalpha():
        if c.islower():
            return chr((ord(c) + n - ord('a')) % 26 + ord('a'))
        else:
            return chr((ord(c) + n - ord('A')) % 26 + ord('A'))
    else:
        return c

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    res = []
    for i in range(len(s)):
        if ord(s[i]) + n > ord('Z'):
            res.append(chr(ord(s[i]) + n - 26))
        else:
            res.append(chr(ord(s[i]) + n))
    print(''.join(res))
