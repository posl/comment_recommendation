Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == "v":
            ans += (n-i-1)*(i+1)
    print(ans)
main()

=======
Suggestion 3

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == 'v' and i != len(S) - 1 and S[i+1] == 'w':
            count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            count += 1

    print(count * (count - 1) // 2)

=======
Suggestion 5

def solve():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            if i == 0:
                continue
            if S[i - 1] == "w":
                count += 1
    print(count)

=======
Suggestion 6

def main():
    s = input()
    print(s.count('vv') + s.count('ww'))

=======
Suggestion 7

def calc(s):
    if len(s) == 1:
        return 1
    v = s.count("v")
    w = s.count("w")
    if v == 0 or w == 0:
        return 0
    return v * w

=======
Suggestion 8

def main():
    s = input()
    print(s.count("vw") + s.count("wv"))

=======
Suggestion 9

def solve():
    s = input()
    print(s.count("vv") + s.count("ww"))

=======
Suggestion 10

def main():
    s = input()
    print(s.count('vv'))
