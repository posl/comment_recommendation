Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    s = set(S)
    t = set(T)
    if len(s) == len(t):
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
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    print("Yes" if sorted(S) == sorted(T) else "No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    S = sorted(S)
    T = sorted(T)
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] > t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #SとTの文字列を集合にして、文字数を比較する
    if len(set(S)) != len(set(T)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return

    # Make a dictionary of characters in S and T
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] in S_dict:
            S_dict[S[i]].append(i)
        else:
            S_dict[S[i]] = [i]
        if T[i] in T_dict:
            T_dict[T[i]].append(i)
        else:
            T_dict[T[i]] = [i]

    # Check if the dictionary values are equal
    if sorted(S_dict.values()) == sorted(T_dict.values()):
        print("Yes")
    else:
        print("No")
