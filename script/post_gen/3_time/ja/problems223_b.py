Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)

=======
Suggestion 2

def main():
    S = input()
    Smin = S
    Smax = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < Smin:
            Smin = S
        if S > Smax:
            Smax = S
    print(Smin)
    print(Smax)

=======
Suggestion 3

def main():
    s = input()
    smin = s
    smax = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < smin:
            smin = s
        if s > smax:
            smax = s
    print(smin)
    print(smax)

=======
Suggestion 4

def main():
    S = input()
    Smin = S
    Smax = S
    for i in range(len(S)):
        S = S[1:] + S[:1]
        if S < Smin:
            Smin = S
        if S > Smax:
            Smax = S
    print(Smin)
    print(Smax)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    smin = s
    smax = s
    for i in range(n):
        s = s[1:] + s[0]
        smin = min(s,smin)
        smax = max(s,smax)
    print(smin)
    print(smax)

=======
Suggestion 6

def solve():
    s = input()
    s_min = s
    s_max = s
    for _ in range(len(s)):
        s = s[1:] + s[0]
        s_min = min(s_min, s)
        s_max = max(s_max, s)
    print(s_min)
    print(s_max)

=======
Suggestion 7

def main():
    # input
    S = input()

    # compute
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        S_min = min(S_min, S)
        S_max = max(S_max, S)

    # output
    print(S_min)
    print(S_max)

=======
Suggestion 8

def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:len(s)] + s[0]
        s_min = min(s_min, s)
        s_max = max(s_max, s)
    print(s_min)
    print(s_max)

=======
Suggestion 9

def main():
    S = input()
    S = list(S)
    S_min = S
    S_max = S
    for i in range(len(S)):
        S.append(S.pop(0))
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
        S = list(S)
    print(''.join(S_min))
    print(''.join(S_max))

=======
Suggestion 10

def shift_left(s):
    return s[1:] + s[0]
