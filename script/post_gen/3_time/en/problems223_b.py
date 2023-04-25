Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    print(min(s[i:] + s[:i] for i in range(len(s))))
    print(max(s[i:] + s[:i] for i in range(len(s))))

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
main()

=======
Suggestion 4

def main():
    S = input()
    S_len = len(S)
    S_min = S
    S_max = S
    for i in range(S_len):
        S = S[-1] + S[:-1]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)

=======
Suggestion 5

def main():
    s = input()
    s_len = len(s)
    s_min = s
    s_max = s
    for i in range(1, s_len):
        s_shift = s[i:] + s[:i]
        if s_shift < s_min:
            s_min = s_shift
        if s_shift > s_max:
            s_max = s_shift
    print(s_min)
    print(s_max)

=======
Suggestion 6

def main():
    S = input()
    T = S+S
    S_min = T
    S_max = ""
    for i in range(len(S)):
        S_max = max(S_max, T[i:i+len(S)])
        S_min = min(S_min, T[i:i+len(S)])
    print(S_min)
    print(S_max)

=======
Suggestion 7

def main():
    s = input()
    s = s + s
    n = len(s)
    m = n//2
    s_min = s
    s_max = s
    for i in range(n):
        s_min = min(s_min, s[i:i+m])
        s_max = max(s_max, s[i:i+m])
    print(s_min)
    print(s_max)

=======
Suggestion 8

def rotate_left(s):
    return s[1:] + s[0]

=======
Suggestion 9

def shift_left(s):
	return s[1:]+s[0]

=======
Suggestion 10

def shift_str(s, n):
    return s[-n:] + s[:-n]
