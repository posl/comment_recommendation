Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

str = input()

=======
Suggestion 2

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 3

def main():
    # input
    S = input()
    # process
    count = 0
    for i in range(len(S)//2):
        if S[i] != S[len(S)-1-i]:
            count += 1
    # output
    print(count)

=======
Suggestion 4

def main():
    str = input()
    count = 0
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            count += 1
    print(count)

=======
Suggestion 5

def check_palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        return s[0] == s[-1] and check_palindrome(s[1:-1])

=======
Suggestion 6

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    s = input()
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            count += 1
    print(count)
