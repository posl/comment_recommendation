Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[1] == T[1] and S[2] == T[2]:
        print('Yes')
    elif S[0] == T[0] and S[1] == T[2] and S[2] == T[1]:
        print('Yes')
    elif S[0] == T[1] and S[1] == T[0] and S[2] == T[2]:
        print('Yes')
    elif S[0] == T[1] and S[1] == T[2] and S[2] == T[0]:
        print('Yes')
    elif S[0] == T[2] and S[1] == T[0] and S[2] == T[1]:
        print('Yes')
    elif S[0] == T[2] and S[1] == T[1] and S[2] == T[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s.count("R") % 2 == t.count("R") % 2 and s.count("G") % 2 == t.count("G") % 2 and s.count("B") % 2 == t.count("B") % 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input().split()
    t = input().split()
    if len(set(s)) == len(set(t)) == 3:
        print('Yes')
    elif len(set(s)) == 2 and len(set(t)) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    elif S[0] == S[1] == S[2] or T[0] == T[1] == T[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
        return
    for i in range(3):
        for j in range(i+1, 3):
            S[i], S[j] = S[j], S[i]
            if S == T:
                print("Yes")
                return
            S[i], S[j] = S[j], S[i]
    print("No")
    return

=======
Suggestion 6

def main():
    S = list(input().split())
    T = list(input().split())
    if S == T:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['R', 'B', 'G']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['G', 'R', 'B']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['R', 'G', 'B']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['G', 'R', 'B']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['R', 'G', 'B']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['R', 'B', 'G']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['G', 'B', 'R'] and T == ['R', 'G

=======
Suggestion 7

def main():
    s = input().split()
    t = input().split()

    if s == t:
        print('Yes')
    elif s[0] == t[0] and s[1] == t[1] and s[2] == t[2]:
        print('Yes')
    elif s[0] == t[1] and s[1] == t[2] and s[2] == t[0]:
        print('Yes')
    elif s[0] == t[2] and s[1] == t[0] and s[2] == t[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input().split()
    T = input().split()
    #print(S)
    #print(T)
    for i in range(3):
        if S[i] == T[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def solve():
    s = input().split()
    t = input().split()
    if s == t:
        print("Yes")
    elif s == t[::-1]:
        print("Yes")
    else:
        print("No")
solve()
