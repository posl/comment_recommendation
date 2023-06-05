Synthesizing 10/10 solutions

=======
Suggestion 1

def move_char(ch, n):
    if not ch.isalpha():
        return ch
    if ch.isupper():
        offset = ord('A')
    else:
        offset = ord('a')

    return chr((ord(ch) - offset + n) % 26 + offset)

=======
Suggestion 2

def move(s, n):
    if n == 0:
        return s
    else:
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(ord(s[i]) + n)
            if ord(s[i]) > ord('Z'):
                s[i] = chr(ord(s[i]) - 26)
        return ''.join(s)

=======
Suggestion 3

def problems146_b():
    n = int(input())
    s = input()
    result = ""
    for i in range(len(s)):
        if s[i] != " ":
            if ord(s[i]) + n > 90:
                result += chr(ord(s[i]) + n - 26)
            else:
                result += chr(ord(s[i]) + n)
        else:
            result += " "
    print(result)

problems146_b()

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    L = list(S)
    for i in range(len(L)):
        L[i] = chr(((ord(L[i])-ord('A'))+N)%26 + ord('A'))
    print(''.join(L))

=======
Suggestion 5

def shift_char(char, n):
    # print("char: ", char)
    # print("n: ", n)
    # print("ord(char): ", ord(char))
    # print("ord(char) + n: ", ord(char) + n)
    # print("ord(char) + n - 65: ", ord(char) + n - 65)
    # print("(ord(char) + n - 65) % 26: ", (ord(char) + n - 65) % 26)
    # print("chr((ord(char) + n - 65) % 26 + 65): ", chr((ord(char) + n - 65) % 26 + 65))
    return chr((ord(char) + n - 65) % 26 + 65)

=======
Suggestion 6

def move_str(s,n):
    a = []
    for i in s:
        if ord(i)+n>90:
            a.append(chr(ord(i)+n-26))
        else:
            a.append(chr(ord(i)+n))
    return ''.join(a)

=======
Suggestion 7

def problem146_b():
    N = int(input())
    S = input()
    result = ""
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            result += chr(ord(S[i]) + N - 26)
        else:
            result += chr(ord(S[i]) + N)
    print(result)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(ord(s[i]) + n - 26), end='')
        else:
            print(chr(ord(s[i]) + n), end='')

=======
Suggestion 9

def problems146_b():
    n = int(input())
    s = input()
    result = ''
    for i in s:
        if ord(i) + n > ord('Z'):
            result += chr(ord(i) + n - ord('Z') + ord('A') - 1)
        else:
            result += chr(ord(i) + n)
    print(result)

=======
Suggestion 10

def move(s, n):
    return chr((ord(s) - ord('A') + n) % 26 + ord('A'))
