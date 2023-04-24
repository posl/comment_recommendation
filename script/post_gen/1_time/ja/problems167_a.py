Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()

    if S == T[0:len(T)-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if T == S + 'z':
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()

    if S == T[:len(S)] and S != T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S in T[:len(T)-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    ans = "Yes"
    if t[0:len(s)] != s:
        ans = "No"
    elif len(set(t)) == len(set(s)):
        ans = "No"
    print(ans)
