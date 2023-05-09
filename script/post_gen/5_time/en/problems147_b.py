Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(len(S)//2):
        if S[i] != S[len(S)-i-1]:
            count += 1
    print(count)

=======
Suggestion 3

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input()

=======
Suggestion 4

def solve():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            ans += 1
    print(ans)
solve()

=======
Suggestion 5

def main():
    S = input()
    count = 0
    for i in range(0, int(len(S)/2)):
        if S[i] != S[-1-i]:
            count += 1
    print(count)

=======
Suggestion 6

def check_palindrome(s):
    return s == s[::-1]

s = input()
count = 0
while not check_palindrome(s):
    s = s[:-1]
    count += 1

print(count)

=======
Suggestion 7

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input()

=======
Suggestion 8

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 9

def main():
    s = input()
    print(len(s) - s.count(s[0]))
