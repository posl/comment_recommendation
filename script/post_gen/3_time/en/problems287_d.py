Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(T) + 1):
        if S[:i].replace('?', 'a') + S[-(len(T) - i):].replace('?', 'a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace('?','a') + S[len(S)-len(T)+i:].replace('?','a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        for j in range(len(T)):
            if S1[j] == T[j] or S1[j] == '?':
                continue
            else:
                print("No")
                break
        else:
            for j in range(len(T)):
                if S2[j] == T[j] or S2[j] == '?':
                    continue
                else:
                    print("No")
                    break
            else:
                print("Yes")
    return

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i].replace('?', '') + s[-(len(t)-i):].replace('?', '') == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        ans = "Yes"
        for j in range(len(T)):
            if T[j] == "?":
                continue
            if S1[j] == "?" or S2[j] == "?":
                continue
            if S1[j] != T[j] and S2[j] != T[j]:
                ans = "No"
                break
        print(ans)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1.count("?") + S2.count("?") + T.count("?") == len(S1) + len(S2) + len(T):
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        S1 = S1.replace('?', 'a')
        S2 = S2.replace('?', 'a')
        if S1 + S2 == T:
            print('Yes')
        else:
            print('No')
    return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1.replace('?','a') == T[:i] and S2.replace('?','a') == T[i:]:
            print('Yes')
        else:
            print('No')
    return

main()

=======
Suggestion 9

def main():
    S = input()
    T = input()
    for i in range(len(T) + 1):
        s = S[:i] + S[-(len(T) - i):]
        if s.replace("?", "") == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def solve():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[-(len(T)-i):]
        if all([s==t or s=='?' or t=='?' for s,t in zip(S_,T)]):
            print('Yes')
        else:
            print('No')
