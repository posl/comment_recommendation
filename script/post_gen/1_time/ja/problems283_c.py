Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == '0':
            ans += 1
        elif s[i] == '1':
            ans += 2
        elif s[i] == '2':
            ans += 3
        elif s[i] == '3':
            ans += 4
        elif s[i] == '4':
            ans += 5
        elif s[i] == '5':
            ans += 6
        elif s[i] == '6':
            ans += 7
        elif s[i] == '7':
            ans += 8
        elif s[i] == '8':
            ans += 9
        elif s[i] == '9':
            ans += 10
    print(ans)

main()

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += int(S[i]) + 1
        else:
            ans += int(S[i]) + 10
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if i == 0 and s[i] == '1':
            ans += 10
        else:
            ans += int(s[i]) + 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        else:
            if int(S[i]) == 0:
                ans += 1
            else:
                ans += int(S[i]) + 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += len(S) - 1
        else:
            ans += 1
        if S[i] != '0':
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    if S == '0':
        print(0)
        return
    ans = 0
    for i in range(len(S)):
        if i == 0:
            if S[i] == '1':
                ans += 1
            elif S[i] == '0':
                ans += 0
            else:
                ans += 2
        else:
            if S[i] == '0':
                ans += 0
            else:
                ans += 1
    ans += len(S) - 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    if N == 1:
        print(int(S))
        return

    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i]) - 1
        else:
            ans += int(S[i])
    ans += N - 1
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    if S == '0':
        print(1)
    else:
        print(len(S))

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    ans = N + (N - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    print(len(S))
