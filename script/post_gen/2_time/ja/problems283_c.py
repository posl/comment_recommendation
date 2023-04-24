Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            continue
        elif i == 0:
            ans += 1
        else:
            ans += 2
        ans += int(S[i])
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "0":
            continue
        else:
            ans += 1
            if i != len(S) - 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = len(s)
    if s[0] == '1':
        ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    if s[0] == '1':
        print(len(s) + 9)
    else:
        print(len(s) + 8)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    S = input().strip()
    ans = 0
    for i in range(len(S)):
        if S[i] == "0":
            continue
        ans += 1
    ans += len(S) - 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    if s == "0":
        print(0)
        return
    print(len(s))

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    print(N)

=======
Suggestion 8

def main():
    S = input()
    print(len(S) + S.count("0") - 1)

=======
Suggestion 9

def main():
    s = input()
    print(len(s))

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    print(N-1 + (N-1)//3)
