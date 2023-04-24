Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace('?','a') + S[-(len(T)-i):].replace('?','a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace('?', 'a') + S[len(S)-len(T)+i:].replace('?', 'a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i] + S[-(len(T)-i):] == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        if S1.count('?') + S2.count('?') == len(T):
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def solve():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace("?", "a") + S[-len(T)+i:].replace("?", "a") == T:
            print("Yes")
        else:
            print("No")

solve()

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-len(T)+i:]
        if S1.count('?') + S2.count('?') + T.count('?') == len(S1) + len(S2) + len(T):
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for x in range(len(t)+1):
        s1 = s[:x]
        s2 = s[len(s)-len(t)+x:]
        if s1.count('?') + s2.count('?') + t.count('?') == len(t) and s1.replace('?','a') + s2.replace('?','a') == t.replace('?','a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for x in range(len(T)+1):
        S1 = S[0:x]
        S2 = S[len(S)-len(T)+x:]
        if S1.count('?') + S2.count('?') + len(T) == len(S):
            for i in range(len(T)):
                if S1[i] != T[i] and S1[i] != '?':
                    break
                if S2[i] != T[i] and S2[i] != '?':
                    break
            else:
                print('Yes')
                continue
        print('No')
    return
