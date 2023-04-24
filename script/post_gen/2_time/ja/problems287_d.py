Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[-(len(t)-i):] == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def match(s,t):
    for i in range(len(t)):
        if s[i] != t[i] and s[i] != '?' and t[i] != '?':
            return False
    return True

s = input()
t = input()

for i in range(len(t)+1):
    if match(s[:i]+s[len(s)-len(t)+i:],t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[len(s)-len(t)+i:]
        s3 = s1+s2
        if s3 == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1+S2 == T.replace('?','a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for x in range(len(T)+1):
        S_prime = S[:x] + S[-(len(T)-x):]
        match = True
        for i in range(len(T)):
            if S_prime[i] != T[i] and S_prime[i] != "?":
                match = False
                break
        if match:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i].replace('?','a') + s[-len(t)+i:].replace('?','a') == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(lt+1):
        if s[i:i+lt] == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[-(len(T)-i):]
        if S_.count("?") + S_.count(T) == len(S_):
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    for x in range(len(t)+1):
        s_ = s[x:len(s)-len(t)+x]
        if s_.count('?') + s_.count(t) == len(s_):
            print('Yes')
        else:
            print('No')
