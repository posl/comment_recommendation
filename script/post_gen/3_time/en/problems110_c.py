Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(T_set):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    S = input()
    T = input()
    
    S_set = set(S)
    T_set = set(T)
    
    if len(S_set) == len(T_set):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    s = sorted(s)
    t = sorted(t, reverse=True)
    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)) == 26:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if len(set(s)) == len(set(t)) == 26:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    if sorted(s) != sorted(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in t[i + 1:]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if sorted(s) != sorted(t):
        print("No")
    else:
        print("Yes")
