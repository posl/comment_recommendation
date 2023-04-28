Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ""
    for c in s:
        ans += chr((ord(c) - ord("A") + n) % 26 + ord("A"))
    print(ans)

=======
Suggestion 2

def shift(s, n):
    return ''.join(chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s)

n = int(input())
s = input()
print(shift(s, n))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr((ord(s) - ord('A') + N) % 26 + ord('A')), end='')
    print()

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s = s[:i] + chr(ord(s[i]) + n - 26) + s[i+1:]
        else:
            s = s[:i] + chr(ord(s[i]) + n) + s[i+1:]
    print(s)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    if n == 0:
        print(s)
    else:
        for i in range(len(s)):
            if ord(s[i]) + n > 90:
                print(chr(ord(s[i]) + n - 26), end="")
            else:
                print(chr(ord(s[i]) + n), end="")
        print()

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    if n == 0:
        print(s)
        return
    for c in s:
        print(chr((ord(c) - ord('A') + n) % 26 + ord('A')), end = '')
    print()

=======
Suggestion 7

def shift(s, shift):
    return ''.join(chr(((ord(c) - ord('A') + shift) % 26) + ord('A')) for c in s)

n = int(input())
s = input()
print(shift(s, n))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in s:
        print(chr((ord(i)-ord('A')+n)%26+ord('A')),end='')
    print()
main()

=======
Suggestion 9

def shift(s, n):
    return ''.join([chr((ord(c) - 65 + n) % 26 + 65) for c in s])

n = int(input())
s = input()
print(shift(s, n))

In the above code, I have used a list comprehension to shift each character in the input string by n . The ord() function returns the ASCII code of a character and chr() function returns the character for a given ASCII code. The modulo operator ( % ) is used to handle the case where the shifted character is beyond Z , which is equivalent to A .

=======
Suggestion 10

def shift_by_n(s, n):
    # Write your code here
    res = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            res += chr(ord(s[i]) + n - 26)
        else:
            res += chr(ord(s[i]) + n)
    return res
