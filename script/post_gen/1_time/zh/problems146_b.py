Synthesizing 10/10 solutions

=======
Suggestion 1

def moveN(s, n):
    l = len(s)
    if n == 0:
        return s
    elif n > 0:
        n = n % 26
        s1 = ''
        for i in range(l):
            if ord(s[i]) + n > 90:
                s1 += chr(ord(s[i]) + n - 26)
            else:
                s1 += chr(ord(s[i]) + n)
        return s1
    else:
        n = n % 26
        s1 = ''
        for i in range(l):
            if ord(s[i]) + n < 65:
                s1 += chr(ord(s[i]) + n + 26)
            else:
                s1 += chr(ord(s[i]) + n)
        return s1

n = int(input())
s = input()
print(moveN(s, n))

=======
Suggestion 2

def main():
    n=int(input())
    s=input()
    s=s.upper()
    for i in range(len(s)):
        if ord(s[i])+n>90:
            print(chr(ord(s[i])+n-26),end='')
        else:
            print(chr(ord(s[i])+n),end='')

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    print(''.join(s))

=======
Suggestion 4

def problems146_b():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(ord(s[i]) + n - 26), end='')
        else:
            print(chr(ord(s[i]) + n), end='')
    print()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for i in s:
        if ord(i)+n > ord('Z'):
            print(chr(ord(i)+n-26),end='')
        else:
            print(chr(ord(i)+n),end='')
    print()

=======
Suggestion 6

def problem146_b():
    N = int(input())
    S = input()
    S = list(S)
    for i in range(len(S)):
        S[i] = chr(ord(S[i]) + N)
        if S[i] > 'Z':
            S[i] = chr(ord(S[i]) - 26)
    print(''.join(S))

=======
Suggestion 7

def rotate(string, n):
    if n == 0:
        return string
    if n > 0:
        n = n % 26
        for i in range(n):
            string = string[1:] + string[0]
        return string
    if n < 0:
        n = abs(n) % 26
        for i in range(n):
            string = string[-1] + string[:-1]
        return string

print(rotate('ABCXYZ', 2))
print(rotate('ABCXYZ', 0))
print(rotate('abcdefghijklmnopqrstuvwxyz', 13))

=======
Suggestion 8

def move_letter(letter, n):
    letter = ord(letter) + n
    if letter > ord('Z'):
        letter = letter - ord('Z') + ord('A') - 1
    return chr(letter)

=======
Suggestion 9

def move(s,n):
    result = ''
    for i in s:
        if ord(i)+n > 90:
            result += chr(ord(i)+n-26)
        else:
            result += chr(ord(i)+n)
    return result

=======
Suggestion 10

def problem146_b():
    N = int(input())
    S = input()

    for i in range(len(S)):
        tmp = ord(S[i]) + N
        if tmp > ord('Z'):
            tmp = tmp - ord('Z') + ord('A') - 1
        print(chr(tmp),end='')
