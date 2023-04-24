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

main()

=======
Suggestion 3

def main():
    s = input()
    min = s
    max = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s < min:
            min = s
        if s > max:
            max = s
    print(min)
    print(max)

main()

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    s_min = s
    s_max = s
    for i in range(n):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 5

def solution(S):
    min = S
    max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min:
            min = S
        if S > max:
            max = S
    return min, max

=======
Suggestion 6

def main():
    s = input()
    l = len(s)
    s = s + s
    smin = s[0:l]
    smax = s[0:l]
    for i in range(1,l):
        if s[i:i+l] < smin:
            smin = s[i:i+l]
        if s[i:i+l] > smax:
            smax = s[i:i+l]
    print(smin)
    print(smax)

=======
Suggestion 7

def main():
    s = input()
    s = s.strip()
    s = s.lower()
    l = len(s)
    s1 = s
    s2 = s
    for i in range(l):
        s1 = s1[1:] + s1[0]
        s2 = s2[-1] + s2[:-1]
        if s1 < s2:
            print(s1)
            print(s2)
            return
    print(s1)
    print(s2)
    return

=======
Suggestion 8

def main():
    #S = list(input())
    S = list("abracadabra")
    Smin = S[:]
    Smax = S[:]
    for i in range(len(S)):
        S.append(S.pop(0))
        Smin = min(Smin, S)
        Smax = max(Smax, S)
    print("".join(Smin))
    print("".join(Smax))
    print("".join(S))

=======
Suggestion 9

def shift_left(s):
    return s[1:] + s[0]

=======
Suggestion 10

def rotate_left(s, n):
    return s[n:] + s[:n]
