Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    S = input()
    T = input()

    # compute

    # output
    if sorted(S) == sorted(T):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort(reverse=True)
    s = ''.join(s_list)
    t = ''.join(t_list)
    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()

    s = list(s)
    t = list(t)

    s.sort()
    t.sort(reverse=True)

    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        for j in range(i+1, len(S)):
            if S[j] == T[i]:
                S = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
                break
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

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
    S = list(S)
    T = list(T)
    S.sort()
    T.sort()
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def solve():
    S = input()
    T = input()
    S1 = sorted(S)
    T1 = sorted(T)
    S2 = sorted(S1)
    T2 = sorted(T1)
    if S1 == T1 and S2 == T2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # input
    s = input()
    t = input()
    # solve
    s = list(s)
    t = list(t)
    s.sort()
    t.sort(reverse=True)
    # output
    if s<t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def check(S,T):
    if len(S) != len(T):
        return False
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            if S[i] in S[i+1:]:
                S = S.replace(S[i],T[i])
            else:
                return False
    return True

S = input()
T = input()
