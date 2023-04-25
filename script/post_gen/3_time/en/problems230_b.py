Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = "oxx" * 10**5
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = 'oxx' * 10**5
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    T = "oxx" * 100000
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = 'oxx' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    T = "oxx" * (10 ** 5)
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = 'o' + 'x' * 5 + 'o' + 'x' * 5 + 'o'
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = "o" * (len(s) // 2) + "x" * (len(s) // 2)
    if len(s) % 2 == 1:
        t = t + "o"
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S = input()
    T = "o" + "x" + "x" * len(S) + "o" * len(S)
    print("Yes" if S in T else "No")

=======
Suggestion 9

def main():
    s = input()
    if s in 'o' * 10**5:
        print('Yes')
    else:
        print('No')
