Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    string = input()
    count = 0
    for i in range(len(string) - 1):
        if string[i] == 'v' and string[i + 1] == 'w':
            count += 1
    print(count)

=======
Suggestion 2

def bottom_count(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count

s = input()
print(bottom_count(s))

=======
Suggestion 3

def count_bottoms(s):
    n = len(s)
    ans = 0
    for i in range(n-1):
        if s[i] == 'v' and s[i+1] == 'w':
            ans += 1
    return ans

=======
Suggestion 4

def count_bottoms(s):
    #print(s)
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count

=======
Suggestion 5

def main():
    s = input()
    #print(s)
    #print(len(s))
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += i
    print(count)

=======
Suggestion 6

def main():
    S = input()
    print(S.count('wv') + S.count('vw'))

=======
Suggestion 7

def problem279_a():
    s = input()
    print(s.count('vw') + s.count('wv'))

=======
Suggestion 8

def main():
    s = input()
    print(s.count("vw"))

=======
Suggestion 9

def main():
    s = raw_input().strip()
    print s.count('vv')

=======
Suggestion 10

def get_input():
    return input()
