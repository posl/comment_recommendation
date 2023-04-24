Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return
    print(len(s)+1)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)
    return

=======
Suggestion 6

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans = i + 1
            break
    if ans == 0:
        ans = len(s) + 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)
main()

This code is contributed by @yukicoder

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(S)+1):
        if S[:i]+S[i:] == T:
            print(i+1)
            break

=======
Suggestion 9

def main():
    S = input()
    T = input()
    # S = "atcoder"
    # T = "atcorder"
    # S = "million"
    # T = "milllion"
    # S = "vvwvw"
    # T = "vvvwvw"
    # S = "abcde"
    # T = "abcde"
    # S = "a"
    # T = "aa"
    # S = "a"
    # T = "ab"
    # S = "a"
    # T = "ba"
    # S = "aa"
    # T = "aaa"
    # S = "aa"
    # T = "aab"
    # S = "aa"
    # T = "aba"
    # S = "aa"
    # T = "baa"
    # S = "aa"
    # T = "baab"
    # S = "aa"
    # T = "bbab"
    # S = "a"
    # T = "ba"
    # S = "a"
    # T = "aa"
    # S = "a"
    # T = "ab"
    # S = "a"
    # T = "aaa"
    # S = "aa"
    # T = "aaa"
    # S = "aa"
    # T = "aab"
    # S = "aa"
    # T = "aba"
    # S = "aa"
    # T = "baa"
    # S = "aa"
    # T = "baab"
    # S = "aa"
    # T = "bbab"
    # S = "a"
    # T = "ba"
    # S = "a"
    # T = "aa"
    # S = "a"
    # T = "ab"
    # S = "a"
    # T = "aaa"
    # S = "aa"
    # T = "aaa"
    # S = "aa"
    # T = "aab"
    # S = "aa"
    # T = "aba"
    # S = "aa"
    # T = "baa"
    # S = "aa"
    # T = "baab"
    # S = "aa"
    # T = "bbab"
    # S = "a"

=======
Suggestion 10

def find_inserted_char(S, T):
    #print(S)
    #print(T)
    S = list(S)
    T = list(T)
    for i in range(len(S)):
        if S[i] != T[i]:
            return i+1
    return len(S)+1
