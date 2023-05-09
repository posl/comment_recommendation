Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
main()

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(0,len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input().strip()
    T = input().strip()
    count = 0
    for i in range(0,len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 6

def solve(S,T):
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    return count
