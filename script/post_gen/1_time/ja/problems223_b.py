Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(min(s[i:] + s[:i] for i in range(len(s))))
    print(max(s[i:] + s[:i] for i in range(len(s))))

=======
Suggestion 2

def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        S_min = min(S_min, S)
        S_max = max(S_max, S)
    print(S_min)
    print(S_max)

=======
Suggestion 3

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
Suggestion 4

def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S_min > S:
            S_min = S
        if S_max < S:
            S_max = S
    print(S_min)
    print(S_max)

=======
Suggestion 5

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
Suggestion 6

def main():
    S = input()
    N = len(S)
    S_min = S
    S_max = S
    for i in range(N):
        S_min = min(S_min, S[i:] + S[:i])
        S_max = max(S_max, S[i:] + S[:i])
    print(S_min)
    print(S_max)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    min_s = S
    max_s = S
    for i in range(N):
        min_s = min(min_s, S[i:] + S[:i])
        max_s = max(max_s, S[i:] + S[:i])
    print(min_s)
    print(max_s)

=======
Suggestion 8

def shift(string, n):
    return string[n:] + string[:n]
