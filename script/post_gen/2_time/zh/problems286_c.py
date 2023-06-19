Synthesizing 10/10 solutions

=======
Suggestion 1

def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return isPalindrome(str[1:-1])

=======
Suggestion 2

def solve():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s1 = s[:n//2]
    s2 = s[n//2+1:]
    s2.reverse()
    ans = 0
    for i in range(n//2):
        if s1[i] != s2[i]:
            if s1[i] == 'a' and s2[i] == 'b':
                ans += a
            elif s1[i] == 'b' and s2[i] == 'a':
                ans += a
            elif s1[i] == 'c' and s2[i] == 'd':
                ans += a
            elif s1[i] == 'd' and s2[i] == 'c':
                ans += a
            elif s1[i] == 'e' and s2[i] == 'f':
                ans += a
            elif s1[i] == 'f' and s2[i] == 'e':
                ans += a
            elif s1[i] == 'g' and s2[i] == 'h':
                ans += a
            elif s1[i] == 'h' and s2[i] == 'g':
                ans += a
            elif s1[i] == 'i' and s2[i] == 'j':
                ans += a
            elif s1[i] == 'j' and s2[i] == 'i':
                ans += a
            elif s1[i] == 'k' and s2[i] == 'l':
                ans += a
            elif s1[i] == 'l' and s2[i] == 'k':
                ans += a
            elif s1[i] == 'm' and s2[i] == 'n':
                ans += a
            elif s1[i] == 'n' and s2[i] == 'm':
                ans += a
            elif s1[i] == 'o' and s2[i] == 'p':
                ans += a
            elif s1[i] == 'p' and s2[i] == 'o':
                ans += a
            elif s1[i] == 'q' and s2[i] == 'r':
                ans += a
            elif s1[i] == 'r' and s2

=======
Suggestion 3

def main():
    input_line = input()
    input_line = input_line.split()
    n = int(input_line[0])
    a = int(input_line[1])
    b = int(input_line[2])
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(n):
        if s[i] == s[n-i-1]:
            continue
        elif s[i] != s[n-i-1]:
            if s[i] == 'a':
                count += a
                s[i] = s[n-i-1]
            elif s[i] == 'b':
                count += b
                s[n-i-1] = s[i]
            elif s[n-i-1] == 'a':
                count += a
                s[n-i-1] = s[i]
            elif s[n-i-1] == 'b':
                count += b
                s[i] = s[n-i-1]
    print(count)

=======
Suggestion 4

def solve(n, a, b, s):
    if n % 2 == 0:
        if a < b:
            return (a * n) // 2
        else:
            return b * n
    else:
        if a < b:
            return a + (a * (n - 1)) // 2
        else:
            return b + b * (n - 1)

=======
Suggestion 5

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    S = input()
    print(S)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s.reverse()
    ans = 0
    for i in range(n):
        if s[i] == s[n-1-i]:
            continue
        elif s[i] == 'a':
            ans += a
        else:
            ans += b
    print(ans)

=======
Suggestion 8

def is_palindrome(s):
    return s == s[::-1]

n, a, b = map(int, input().split())
s = input()

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        if a <= b:
            print(a * n // 2)
        else:
            print(b * n // 2)
    else:
        if a <= b:
            print(a * (n - 1) // 2 + b)
        else:
            print(b * (n - 1) // 2 + b)

=======
Suggestion 10

def problem286_c():
    pass
