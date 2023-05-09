Synthesizing 10/10 solutions (Duplicates hidden)

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
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 4

def main():
    S = input()
    min_str = S
    max_str = S
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if min_str > S:
            min_str = S
        if max_str < S:
            max_str = S
    print(min_str)
    print(max_str)

main()

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    s1 = s
    s2 = s
    for i in range(n):
        s1 = s1[1:] + s1[0]
        s2 = s2[-1] + s2[:-1]
        if s1 < s2:
            print(s1)
            print(s2)
            break
    else:
        print(s1)
        print(s2)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    s = s+s
    print(min([s[i:i+n] for i in range(n)]))
    print(max([s[i:i+n] for i in range(n)]))

=======
Suggestion 7

def solve(S):
    # Complete this function
    l = len(S)
    min = S
    max = S
    for i in range(l):
        str = S[i:l] + S[0:i]
        if str < min:
            min = str
        if str > max:
            max = str
    return min, max

=======
Suggestion 8

def shift_left(s):
    return s[1:]+s[0]

=======
Suggestion 9

def shiftLeft(s):
    return s[1:] + s[0]
