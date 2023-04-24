Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = ''
    for s in S:
        ans += chr((ord(s) - ord('A') + N) % 26 + ord('A'))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    for i in s:
        print(chr((ord(i) - ord('A') + n) % 26 + ord('A')), end='')
    print()

=======
Suggestion 4

def shift(s, n):
    return ''.join([chr((ord(x) - ord('A') + n) % 26 + ord('A')) for x in s])

N = int(input())
S = input()
print(shift(S, N))

I have a problem with the following code. It works fine for the first test case but gives a wrong answer for the second test case. I don't know what's wrong with it. Can someone help me?

Here's the code:

n = int(input())
s = input()
s = s.upper()
l = []
for i in range(0,len(s)):
    if s[i] == " ":
        l.append(s[i])
    else:
        l.append(chr((ord(s[i])+n-65)%26+65))
print(*l, sep="")

Here's the first test case:

2
ABC XYZ

Here's the second test case:

3
ABC XYZ

Here's the output for the first test case:

CDE ZAB

Here's the output for the second test case:

DEF ZAB

I have a problem with the following code. It works fine for the first test case but gives a wrong answer for the second test case. I don't know what's wrong with it. Can someone help me?

Here's the code:

n = int(input())
s = input()
s = s.upper()
l = []
for i in range(0,len(s)):
    if s[i] == " ":
        l.append(s[i])
    else:
        l.append(chr((ord(s[i])+n-65)%26+65))
print(*l, sep="")

Here's the first test case:

2
ABC XYZ

Here's the second test case:

3
ABC XYZ

Here's the output for the first test case:

CDE ZAB

Here's the output for the second test case:

DEF ZAB

Here is the problem: https://atcoder.jp/contests/abc208/tasks/abc208_a

I am trying to solve this problem using Python. I have the following code:

a,b = map(int,input().split())

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for c in s:
        if c == ' ':
            print(' ', end='')
        else:
            print(chr(ord('A') + (ord(c) - ord('A') + n) % 26), end='')
    print()

=======
Suggestion 6

def shift_char(char, shift):
    if char.isalpha():
        if ord(char) + shift > ord('Z'):
            return chr(ord(char) + shift - 26)
        else:
            return chr(ord(char) + shift)
    else:
        return char

=======
Suggestion 7

def shift(n, s):
    result = ""
    for c in s:
        if ord(c) + n > ord("Z"):
            result += chr(ord("A") + ord(c) + n - ord("Z") - 1)
        else:
            result += chr(ord(c) + n)
    return result

=======
Suggestion 8

def shift(s, n):
    if n == 0:
        return s
    if n > 26:
        n = n % 26
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    return ''.join(s)

N = int(input())
S = input()
print(shift(S, N))

This is my code for this problem.

I'm not sure if this is the best solution, but it works.

I'm interested in your opinion.

Thanks.

I think it is good. I think it is good.

I think it is good.

=======
Suggestion 9

def shift_alphabet(s, n):
    if s.isalpha():
        if ord(s) + n <= ord("Z"):
            return chr(ord(s) + n)
        else:
            return chr(ord(s) + n - 26)
    else:
        return s

=======
Suggestion 10

def shift(n, s):
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B)
    # shift each letter of s by n in alphabetical order
    # we assume that A follows Z
    # for example, shifting A by 2 results in C (A -> B -> C)
    # and shifting Y by 3 results in B (Y -> Z -> A -> B
