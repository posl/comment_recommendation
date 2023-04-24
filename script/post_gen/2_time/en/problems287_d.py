Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace('?', 'a') + S[-(len(T)-i):].replace('?', 'a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(t) + 1):
        if s[:i].replace('?', 'a') + s[-(len(t) - i):].replace('?', 'a') == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace('?', 'a') + S[len(S)-len(T)+i:].replace('?', 'a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(T) + 1):
        if S[:i] + S[-len(T) + i:] == T.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for x in range(len(T) + 1):
        S1 = S[:x]
        S2 = S[len(S) - len(T) + x:]
        S3 = S1 + S2
        if all(T[i] == S3[i] or T[i] == '?' or S3[i] == '?' for i in range(len(T))):
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[len(S)-len(T)+i:]
        if S_.replace('?', '') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if '?' in s1:
            s1 = s1.replace('?', 'a')
        if '?' in s2:
            s2 = s2.replace('?', 'a')
        if s1+s2 == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        if all([s1 == t1 or s1 == "?" or t1 == "?" for s1, t1 in zip(S1, T[:i])]) and all([s2 == t2 or s2 == "?" or t2 == "?" for s2, t2 in zip(S2, T[i:])]):
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def solve():
    s = list(input())
    t = list(input())
    for i in range(len(t)+1):
        if s[i:i+len(t)] == t or s[i:i+len(t)] == ['?']*len(t):
            print('Yes')
        else:
            print('No')
