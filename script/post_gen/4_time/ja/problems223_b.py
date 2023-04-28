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
main()

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
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        s_min = min(s_min, s)
        s_max = max(s_max, s)
    print(s_min)
    print(s_max)

=======
Suggestion 5

def main():
    s = input()
    slen = len(s)
    smin = s
    smax = s
    for i in range(slen):
        s = s[1:] + s[0]
        if s < smin:
            smin = s
        if s > smax:
            smax = s
    print(smin)
    print(smax)

=======
Suggestion 6

def main():
    S = input()
    S_len = len(S)
    S_min = S
    S_max = S
    for i in range(S_len):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)

=======
Suggestion 7

def main():
    s = input()
    min_str = s
    max_str = s
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if min_str > tmp:
            min_str = tmp
        if max_str < tmp:
            max_str = tmp
    print(min_str)
    print(max_str)

=======
Suggestion 8

def main():
    s = input()
    s = list(s)
    s_min = s
    s_max = s
    for i in range(len(s)):
        s.append(s.pop(0))
        if s < s_min:
            s_min = s
        if s > s_max:
            s_max = s
    print(''.join(s_min))
    print(''.join(s_max))
