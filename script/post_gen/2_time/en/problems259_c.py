Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N != M:
        print("No")
        return
    for i in range(N):
        if S[i] != T[i]:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("Yes")
    return

main()

I think this is a good problem.

I solved this problem using Python3.

I got 100 points.

This is my first post.

I will continue to post my solutions.

I hope you like this article.

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if len(S) >= len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    if S[-1] != T[len(S)]:
        print("No")
        return
    print("Yes")

=======
Suggestion 3

def main():
    S = input()
    T = input()

    if len(S) > len(T):
        print("No")
        return

    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print("Yes")
            return
        print("No")
        return
    print("Yes")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if len(S) < len(T):
        print('No')
        return
    i = 0
    j = 0
    while i < len(S):
        if j < len(T) and S[i] == T[j]:
            j += 1
        i += 1
    if j == len(T):
        print('Yes')
    else:
        print('No')

main()

I think this is a bit more readable than the other solutions I've seen, and it passes all the test cases.

=======
Suggestion 6

def main():
    S = input()
    T = input()
    S = S.replace('a','1').replace('b','2').replace('c','3')
    T = T.replace('a','1').replace('b','2').replace('c','3')
    print('Yes' if S == T else 'No')
main()

=======
Suggestion 7

def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i+1:] == T[i+1:]:
            print("Yes")
            return
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    s = input()
    t = input()
    print("Yes" if solve(s, t) else "No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    S = S + ' '
    T = T + ' '
    s = 0
    t = 0
    while s < len(S) - 1 and t < len(T) - 1:
        if S[s] == T[t]:
            s += 1
            t += 1
        elif S[s + 1] == T[t]:
            s += 1
        elif S[s] == T[t + 1]:
            t += 1
        else:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def solve(s,t):
    if len(s) < len(t):
        return "No"
    for i in range(len(s)):
        if i == len(t):
            return "Yes"
        if s[i] != t[i]:
            if i == 0 or s[i-1] != t[i]:
                return "No"
    return "Yes"

s = input()
t = input()
print(solve(s,t))
