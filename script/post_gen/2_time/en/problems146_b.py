Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            ans += chr(ord(s[i]) + n - 26)
        else:
            ans += chr(ord(s[i]) + n)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    for c in s:
        print(chr((ord(c) - ord('A') + n) % 26 + ord('A')), end = '')
    print()

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    print(''.join([chr((ord(c)-ord('A')+n)%26+ord('A')) for c in s]))

=======
Suggestion 5

def shift(s, n):
  return ''.join(chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s)

n = int(input())
s = input()
print(shift(s, n))

Python 3.6.1 (default, Apr  4 2017, 09:40:21) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import string
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> ord('A')
65
>>> ord('Z')
90
>>> ord('A') - ord('A')
0
>>> ord('A') - ord('A') + 1
1
>>> ord('Z') - ord('A') + 1
26
>>> ord('Z') - ord('A') + 2
27
>>> ord('Z') - ord('A') + 3
28
>>> ord('Z') - ord('A') + 4
29
>>> ord('Z') - ord('A') + 5
30
>>> ord('Z') - ord('A') + 6
31
>>> ord('Z') - ord('A') + 7
32
>>> ord('Z') - ord('A') + 8
33
>>> ord('Z') - ord('A') + 9
34
>>> ord('Z') - ord('A') + 10
35
>>> ord('Z') - ord('A') + 11
36
>>> ord('Z') - ord('A') + 12
37
>>> ord('Z') - ord('A') + 13
38
>>> ord('Z') - ord('A') + 14
39
>>> ord('Z') - ord('A') + 15
40
>>> ord('Z') - ord('A') + 16
41
>>> ord('Z') - ord('A') + 17
42
>>> ord('Z') - ord('A') + 18
43
>>> ord('Z') - ord('A') + 19
44
>>> ord('Z') - ord('A') + 20
45
>>>

=======
Suggestion 6

def shift_char(c, n):
    if ord(c) + n > ord('Z'):
        return chr(ord(c) + n - 26)
    else:
        return chr(ord(c) + n)

n = int(input())
s = input()

for c in s:
    print(shift_char(c, n), end="")

Related

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for c in S:
        print(chr((ord(c)-ord('A')+N)%26+ord('A')),end='')
    print()

=======
Suggestion 8

def shift(s,n):
    return ''.join([chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s])

n = int(input())
s = input()
print(shift(s,n))

=======
Suggestion 9

def shift_char(char, n):
    if char == " ":
        return char
    else:
        return chr((ord(char) - ord("A") + n) % 26 + ord("A"))

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    S = S.upper()
    S = S.replace(" ", "")
    S = S.replace(".", "")
    S = S.replace(",", "")
    S = S.replace(":", "")
    S = S.replace(";", "")
    S = S.replace("!", "")
    S = S.replace("?", "")
    S = S.replace("-", "")
    S = S.replace("'", "")
    S = S.replace('"', "")
    S = S.replace("(", "")
    S = S.replace(")", "")
    S = S.replace("[", "")
    S = S.replace("]", "")
    S = S.replace("{", "")
    S = S.replace("}", "")
    S = S.replace("/", "")
    S = S.replace("\\", "")
    S = S.replace("*", "")
    S = S.replace("&", "")
    S = S.replace("^", "")
    S = S.replace("%", "")
    S = S.replace("$", "")
    S = S.replace("#", "")
    S = S.replace("@", "")
    S = S.replace("`", "")
    S = S.replace("~", "")
    S = S.replace("_", "")
    S = S.replace("=", "")
    S = S.replace("+", "")
    S = S.replace("|", "")
    S = S.replace("0", "")
    S = S.replace("1", "")
    S = S.replace("2", "")
    S = S.replace("3", "")
    S = S.replace("4", "")
    S = S.replace("5", "")
    S = S.replace("6", "")
    S = S.replace("7", "")
    S = S.replace("8", "")
    S = S.replace("9", "")
    S = S.replace("1", "")
    S = S.replace("2", "")
    S = S.replace("3", "")
    S = S.replace("4", "")
    S = S.replace("5", "")
    S = S.replace("6", "")
    S = S.replace("7", "")
    S = S.replace("8", "")
    S = S.replace("9", "")
    S = S.replace("1", "")
    S = S.replace("2", "")
    S = S.replace("3", "")
    S = S.replace("4", "")
    S = S.replace("5", "")
    S = S.replace("6", "")
    S = S.replace("7", "")
    S = S
