Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    S = input()
    T = input()

    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1

    print(diff)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print(sum(s != t for s, t in zip(S, T)))

main()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    print(sum(si != ti for si, ti in zip(s, t)))

=======
Suggestion 9

def main():
    S = input()
    T = input()
    print(sum([1 for s, t in zip(S, T) if s != t]))
