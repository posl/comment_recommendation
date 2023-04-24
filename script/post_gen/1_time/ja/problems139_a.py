Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()

    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1

    print(count)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)
    return
