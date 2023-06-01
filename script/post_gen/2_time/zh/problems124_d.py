Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0' and i % 2 == 0:
            count += 1
        elif s[i] == '1' and i % 2 == 1:
            count += 1
    print(min(count, len(s) - count))

=======
Suggestion 2

def main():
    s = input()
    s1 = s[::2]
    s2 = s[1::2]
    s3 = s[1::2]
    s4 = s[::2]
    n1 = 0
    n2 = 0
    for i in range(len(s)):
        if s[i] == s1[i]:
            n1 += 1
        if s[i] == s2[i]:
            n2 += 1
    print(min(n1, n2))

=======
Suggestion 3

def problems124_c():
    pass

=======
Suggestion 4

def main():
    s = input()
    s = s.strip()
    if len(s) == 1:
        print(0)
        return
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
    print(min(count, len(s) - count))

=======
Suggestion 6

def solution(s):
    s = s.strip()
    if len(s) == 1:
        return 0
    else:
        count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
        return count

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    if n == 1:
        print(0)
    else:
        print(min(s.count('0'),s.count('1'))*2)

=======
Suggestion 8

def solve():
    s = input()
    s = s.replace("01", "0 1").replace("10", "1 0").split()
    print(min(len(s[::2]), len(s[1::2])))

=======
Suggestion 9

def solve(s):
    a = s.count("0")
    b = s.count("1")
    return min(a,b)*2

=======
Suggestion 10

def main():
    s = input()
    white = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "1":
                white += 1
        else:
            if s[i] == "0":
                white += 1
    print(min(white, len(s) - white))
