Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '+':
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

=======
Suggestion 3

def main():
    S = input()
    result = 0
    for i in range(4):
        if S[i] == '+':
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 4

def main():
    S = input()
    result = 0
    for i in range(len(S)):
        if S[i] == "+":
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 5

def main():
    s = input()
    cnt = 0
    for i in s:
        if i == '+':
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

=======
Suggestion 6

def main():
    S = input()
    count = 0
    for i in S:
        if i == "+":
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 7

def main():
    s = input()
    n = 0
    for i in range(4):
        if s[i] == '+':
            n += 1
        else:
            n -= 1
    print(n)

=======
Suggestion 8

def main():
    # input
    S = input()
    # compute
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    # output
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    print(s.count('+') - s.count('-'))
