Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    if count <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[i]):
            print("No")
            return
    print("Yes")

=======
Suggestion 4

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
Suggestion 5

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if sorted(S) != sorted(T):
        print("No")
        return
    print("Yes")

=======
Suggestion 6

def main():
    S = input()
    T = input()

    for i in range(len(S)):
        if S[i] != T[i]:
            if S.count(S[i]) != T.count(T[i]):
                print("No")
                return
    print("Yes")

main()

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        elif S[i] in T and T[i] in S:
            continue
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    if sorted(S) != sorted(T):
        print("No")
        return
    print("Yes")

=======
Suggestion 9

def main():
    S = input()
    T = input()

    #print(S)
    #print(T)

    S_list = list(S)
    T_list = list(T)

    #print(S_list)
    #print(T_list)

    S_set = set(S_list)
    T_set = set(T_list)

    #print(S_set)
    #print(T_set)

    if len(S_set) < len(T_set):
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def main():
    S = input()
    T = input()

    #print(S, T)
    S = list(S)
    T = list(T)
    #print(S, T)

    S.sort()
    T.sort()
    #print(S, T)

    if S == T:
        print('Yes')
    else:
        print('No')
