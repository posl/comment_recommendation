Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            ans += 1
    print(ans)
solve()

=======
Suggestion 2

def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            count += s[i+1:].count("w")
    print(count)

=======
Suggestion 6

def main():
    S = input()
    stack = []
    count = 0
    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
        elif stack[-1] == S[i]:
            stack.append(S[i])
        else:
            stack.pop()
            count += 1
    print(count)

=======
Suggestion 7

def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "v":
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    print(s.count('vv') + s.count('ww'))

=======
Suggestion 9

def main():
    s = input()
    print(s.count("vv") + s.count("ww"))

=======
Suggestion 10

def solve():
    s = input()
    print(s.count("vv"))
