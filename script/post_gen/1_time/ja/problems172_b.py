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
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    #S = "cupofcoffee"
    #T = "cupofhottea"
    #S = "abcde"
    #T = "bcdea"
    #S = "apple"
    #T = "apple"
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)
