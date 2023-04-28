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
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 4

def main():
    s = input()
    s_len = len(s)
    s_min = s
    s_max = s
    for i in range(s_len):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    mn = s
    mx = s
    for i in range(n):
        s = s[1:] + s[0]
        mn = min(mn, s)
        mx = max(mx, s)
    print(mn)
    print(mx)

=======
Suggestion 6

def main():
    S = input()
    T = S
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S < T:
            T = S
    print(T)
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S > T:
            T = S
    print(T)

=======
Suggestion 7

def shift(string, n):
    return string[n:] + string[:n]

string = input()
strings = [shift(string, i) for i in range(len(string))]
print(min(strings))
print(max(strings))

=======
Suggestion 8

def main():
    s = input()
    s = list(s)
    n = len(s)
    s1 = s[1:]
    s1.append(s[0])
    s2 = s[n-1:] + s[:n-1]
    print(min(''.join(s1), ''.join(s2)))
    print(max(''.join(s1), ''.join(s2)))

=======
Suggestion 9

def shift_left(s):
    return s[1:] + s[0]

=======
Suggestion 10

def shiftLeft(s):
    return s[1:] + s[0]
