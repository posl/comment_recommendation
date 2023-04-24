Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[-len(t)+i:] == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i]+S[-len(T)+i:] == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[len(s)-len(t)+i:] == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[i:i+len(T)] == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[len(S)-len(T)+i:]
        for j in range(len(T)):
            if S_[j] == '?' or S_[j] == T[j]:
                continue
            else:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 6

def main():
    S = input()
    T = input()

    for i in range(len(T) + 1):
        if S[:i] + S[-len(T) + i:] == T.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[0:i]
        S2 = S[len(S)-len(T)+i:]
        if S1+S2 == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].endswith(T[:i]):
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if s1.count("?") + s2.count("?") + len(t) - i - s1.count("?") - s2.count("?") == len(t):
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[i:-(len(T)-i)]
        if S_.count('?') == len(T):
            print('Yes')
        else:
            print('No')
