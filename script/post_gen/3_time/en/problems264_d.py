Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += abs(ord(s[i]) - ord(t[i]))
    print(ans)

main()

=======
Suggestion 2

def main():
    S = input()
    T = "atcoder"
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += abs(ord(S[i]) - ord(T[i]))
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(S)):
        if S[i] != atcoder[i]:
            ans += abs(ord(S[i]) - ord(atcoder[i]))
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    atcoder = "atcoder"
    ans = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            ans += len(s) - i - 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    t = 'atcoder'
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += n - i - 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    t = 'atcoder'
    if s == t:
        print(0)
        return
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += len(s) - i - 1
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] != t[i]:
            ans += i
            break
    print(ans)

=======
Suggestion 7

def main():
    s = list(input())
    atcoder = list("atcoder")
    ans = 0
    for i in range(7):
        for j in range(i, 8):
            if s[i] == atcoder[j]:
                ans += j - i
                s[i], s[j] = s[j], s[i]
                break
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    atcoder = "atcoder"
    res = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            res += 1
    print(res)
main()

=======
Suggestion 9

def main():
    s = input()
    goal = "atcoder"
    ans = 0
    for i in range(7):
        if s[i] != goal[i]:
            for j in range(7, i, -1):
                if s[j] == goal[i]:
                    ans += j - i
                    s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                    break
    print(ans)

main()

=======
Suggestion 10

def count_swaps(s):
    if len(s) < 2:
        return 0
    if len(s) == 2:
        if s[0] == 'a':
            if s[1] == 't':
                return 0
            else:
                return 1
        else:
            return 2
    if s[0] == 'a':
        return count_swaps(s[1:])
    else:
        return 1 + count_swaps(s[1:])

s = input()
print(count_swaps(s))
