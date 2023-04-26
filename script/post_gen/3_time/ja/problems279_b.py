Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    S = input()
    T = input()
    if len(S) < len(T):
        print("No")
        return
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def check(s,t):
    if len(t) > len(s):
        return False
    for i in range(len(s)):
        if s[i] == t[0]:
            if s[i:i+len(t)] == t:
                return True
    return False

s = input()
t = input()

=======
Suggestion 6

def check_substring(s, t):
    i = 0
    while i < len(s):
        if s[i:i+len(t)] == t:
            return True
        i += 1
    return False

=======
Suggestion 7

def main():
    s = input()
    t = input()
    #print(s)
    #print(t)
    if len(s) < len(t):
        print('No')
    else:
        for i in range(len(s)):
            if s[i] == t[0]:
                #print(s[i:i+len(t)])
                if s[i:i+len(t)] == t:
                    print('Yes')
                    break
        else:
            print('No')
