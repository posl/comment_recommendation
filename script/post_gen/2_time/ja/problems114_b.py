Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 1000
    for i in range(len(S)-2):
        ans = min(ans, abs(int(S[i:i+3])-753))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 999
    for i in range(len(S)-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    min_diff = 753
    for i in range(len(S) - 2):
        diff = abs(int(S[i:i + 3]) - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 4

def main():
    s = input()
    ans = 999
    for i in range(len(s)-2):
        ans = min(ans, abs(int(s[i:i+3])-753))
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = 1000
    for i in range(N-2):
        ans = min(ans, abs(int(S[i:i+3]) - 753))
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    min_diff = 1000
    for i in range(len(s) - 2):
        x = int(s[i:i+3])
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

main()

=======
Suggestion 7

def main():
    s = input()
    x = []
    for i in range(len(s) - 2):
        x.append(abs(int(s[i:i+3]) - 753))
    print(min(x))

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    min_diff = 999
    for i in range(N-2):
        X = int(S[i:i+3])
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 9

def main():
    s = input()
    d = []
    for i in range(len(s)-2):
        d.append(abs(753 - int(s[i:i+3])))
    print(min(d))

=======
Suggestion 10

def main():
    S = input()
    an
