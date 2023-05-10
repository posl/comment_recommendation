Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 753
    for i in range(len(S)-2):
        ans = min(ans, abs(753-int(S[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    min_dif = 753
    for i in range(len(s) - 2):
        dif = abs(int(s[i:i+3]) - 753)
        if dif < min_dif:
            min_dif = dif
    print(min_dif)

=======
Suggestion 3

def main():
    s = input().rstrip()
    min = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < min:
            min = abs(x-753)
    print(min)

=======
Suggestion 4

def main():
    S = input()
    min_diff = 999
    for i in range(0,len(S)-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 5

def main():
    S = input()
    S_len = len(S)
    min_diff = 1000
    for i in range(S_len-2):
        diff = abs(753 - int(S[i:i+3]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    s = input()
    ans = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < ans:
            ans = abs(x-753)
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    ans = 999
    for i in range(len(s)-2):
        ans = min(ans, abs(int(s[i:i+3])-753))
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    ans = 999
    for i in range(N-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < ans:
            ans = diff
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    min = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < min:
            min = abs(x-753)
    print(min)

=======
Suggestion 10

def main():
    s = input()
    x = 753
    for i in range(len(s) - 2):
        if abs(int(s[i:i+3]) - 753) < x:
            x = abs(int(s[i:i+3]) - 753)
    print(x)
