Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    for i in s:
        if i == "+":
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    result = 0
    for i in range(len(s)):
        if s[i] == "+":
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 6

def main():
    s = input()
    result = 0
    for i in range(4):
        if s[i] == "+":
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 7

def main():
    s = input()
    result = 0
    for i in s:
        if i == "+":
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 8

def main():
    S = input()
    ans = 0
    for i in S:
        if i == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 10

def main():
    S = input()
    print(S.count('+') - S.count('-'))
