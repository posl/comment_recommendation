Synthesizing 10/10 solutions

=======
Suggestion 1

def move(s,n):
    s = s.upper()
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    s = ''.join(s)
    return s

=======
Suggestion 2

def move(s,n):
    result = ''
    for i in s:
        if ord(i)+n>90:
            result += chr(ord(i)+n-26)
        else:
            result += chr(ord(i)+n)
    return result

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    result = []
    for i in S:
        if ord(i) + N > ord('Z'):
            result.append(chr(ord(i) + N - ord('Z') + ord('A') - 1))
        else:
            result.append(chr(ord(i) + N))
    print(''.join(result))

=======
Suggestion 4

def shift(s,n):
    result = ""
    for c in s:
        if ord(c) + n > ord('Z'):
            result += chr(ord(c) + n - ord('Z') + ord('A') - 1)
        else:
            result += chr(ord(c) + n)
    return result

=======
Suggestion 5

def move_char(c, n):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        if ord(c) + n > ord('Z'):
            return chr(ord('A') + n - (ord('Z') - ord(c)) - 1)
        else:
            return chr(ord(c) + n)
    else:
        return c

=======
Suggestion 6

def move(str,n):
    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str2 = 'abcdefghijklmnopqrstuvwxyz'
    str3 = ''
    for s in str:
        if s in str1:
            str3 += str1[(str1.index(s)+n)%26]
        elif s in str2:
            str3 += str2[(str2.index(s)+n)%26]
        else:
            str3 += s
    return str3

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ret = ""
    for c in s:
        x = ord(c) + n
        if x > ord('Z'):
            x = x - ord('Z') + ord('A') - 1
        ret += chr(x)
    print(ret)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    result = []
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            result.append(chr(ord(s[i]) + n - 26))
        else:
            result.append(chr(ord(s[i]) + n))
    print(''.join(result))

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(64 + ord(s[i]) + n - 90), end='')
        else:
            print(chr(ord(s[i]) + n), end='')
    print()

=======
Suggestion 10

def main():
    n = int(input())
    S = input()
    S = S.upper()
    s_list = list(S)
    for i in range(len(s_list)):
        s_list[i] = chr(ord(s_list[i]) + n)
        if ord(s_list[i]) > ord('Z'):
            s_list[i] = chr(ord(s_list[i]) - ord('Z') + ord('A') - 1)
    print(''.join(s_list))
