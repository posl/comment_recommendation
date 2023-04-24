Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    s = sorted(s)
    t = sorted(t, reverse=True)
    if s < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[i]):
            print('No')
            exit()
    print('Yes')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S.count(S[i]) != T.count(T[i]):
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    S = input()
    T = input()

    S = list(S)
    T = list(T)

    S.sort()
    T.sort(reverse=True)

    if S < T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    print('Yes' if sorted(S) == sorted(T) else 'No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    if len(set(S)) == len(set(T)):
        print("Yes")
        return
    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    print('Yes' if len(set(s)) == len(set(t)) else 'No')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    S = sorted(S)
    T = sorted(T)
    print('Yes' if S == T else 'No')

=======
Suggestion 10

def main():
    S = input()
    T = input()

    # ソートした結果が一致するかどうかで判定
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")
