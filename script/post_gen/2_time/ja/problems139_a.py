Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

main()

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
    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    ans = 0
    for s, t in zip(S, T):
        if s == t:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(3) if S[i] == T[i]]))
