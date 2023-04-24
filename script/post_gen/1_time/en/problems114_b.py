Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 753
    for i in range(len(s)-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = 999
    for i in range(N-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    ans = 999
    for i in range(len(S)-2):
        ans = min(ans,abs(753-int(S[i:i+3])))
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    min_diff = 753
    for i in range(len(S)-2):
        min_diff = min(min_diff, abs(753 - int(S[i:i+3])))
    print(min_diff)

=======
Suggestion 5

def solve(s):
    min = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(753-x) < min:
            min = abs(753-x)
    return min

=======
Suggestion 6

def main():
    S = input()
    print(min(abs(int(S[i:i+3])-753) for i in range(len(S)-2)))

=======
Suggestion 7

def main():
    S = input()
    S = [int(c) for c in S]
    min_diff = 1000
    for i in range(len(S)-2):
        X = S[i] * 100 + S[i+1] * 10 + S[i+2]
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    S = input()
    S = list(S)
    S = [int(s) for s in S]
    ans = 999
    for i in range(len(S)-2):
        tmp = int(str(S[i]) + str(S[i+1]) + str(S[i+2]))
        ans = min(ans, abs(tmp - 753))
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    S = list(S)
    S = [int(i) for i in S]
    #print(S)
    #print(len(S))
    min_diff = 999
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        #print(X)
        diff = abs(X - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 10

def main():
    S = input()
    S = list
