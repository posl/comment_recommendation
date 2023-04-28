Synthesizing 10/10 solutions (Duplicates hidden)

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
    if sorted(s) == sorted(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    ss = set(s)
    tt = set(t)
    if len(ss) == len(tt):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(set(s)) == len(set(t)) == 26:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if len(s) == 1:
        if s == t:
            print("Yes")
        else:
            print("No")
        return
    s_list = sorted(list(s))
    t_list = sorted(list(t))
    s_list = [s_list[i] for i in range(len(s_list)) if i == 0 or s_list[i] != s_list[i-1]]
    t_list = [t_list[i] for i in range(len(t_list)) if i == 0 or t_list[i] != t_list[i-1]]
    if len(s_list) == len(t_list):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    s = sorted(s)
    t = sorted(t)
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def solve(s, t):
    return 'Yes' if set(s) == set(t) else 'No'

s = input()
t = input()
print(solve(s, t))
