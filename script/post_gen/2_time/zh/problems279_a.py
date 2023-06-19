Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'w' and i != len(s) - 1:
            if s[i + 1] == 'w':
                count += 1
    print(count)

=======
Suggestion 2

def count_d(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += s.count('v', i+1, len(s))
    return count

=======
Suggestion 3

def count_bottom(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'v':
            for j in range(i,len(str)):
                if str[j] == 'v':
                    count += 1
    return count

=======
Suggestion 4

def main():
    s = input()
    print(s.count('wv'))

=======
Suggestion 5

def count(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            for j in range(i+1,len(s)):
                if s[j] == "v":
                    count += 1
    return count

=======
Suggestion 6

def main():
    s = input()
    print(s.count('vv'))

=======
Suggestion 7

def main():
    s = input()
    print(s.count("vv"))

=======
Suggestion 8

def count_vw(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count

=======
Suggestion 9

def main():
    s = input()
    print(s.count('vw') + s.count('wv'))

=======
Suggestion 10

def count(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            for j in range(i+1,len(s)):
                if s[j] == 'w':
                    count += 1
    return count
