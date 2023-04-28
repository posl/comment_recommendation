Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    s = input()
    l = len(s)
    count = 0
    for i in range(int(l/2)):
        if s[i] != s[l-i-1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)//2):
        if(s[i] != s[len(s)-i-1]):
            count += 1
    print(count)

=======
Suggestion 4

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input()

=======
Suggestion 5

def is_palindrome(s):
    return s == s[::-1]

s = input()
l = len(s)
c = 0
for i in range(l//2):
    if s[i] != s[l-i-1]:
        c += 1
print(c)

=======
Suggestion 6

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

S = input()

=======
Suggestion 7

def is_palindrome(word):
    return word == word[::-1]

S = input()
count = 0
while not is_palindrome(S):
    S = S[0:-1]
    count += 1
print(count)

=======
Suggestion 8

def is_palindrome(s):
    return s == s[::-1]

s = input()

=======
Suggestion 9

def is_palindrome(s):
    return s == s[::-1]

s = input()
n = len(s)
