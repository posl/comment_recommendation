Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        ans = min(ans, abs(753-x))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 1000
    for i in range(len(S)-2):
        ans = min(ans, abs(753-int(S[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = 753
    for i in range(len(s)-2):
        ans = min(ans,abs(753-int(s[i:i+3])))
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    min = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)

=======
Suggestion 5

def main():
    # input
    S = input()

    # compute
    X = []
    for i in range(len(S)-2):
        X.append(abs(753-int(S[i:i+3])))

    # output
    print(min(X))

=======
Suggestion 6

def main():
    s = input()
    x = 753
    for i in range(len(s)-2):
        x = min(x,abs(753-int(s[i:i+3])))
    print(x)

=======
Suggestion 7

def main():
    S = input()
    result = 999
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        result = min(result, abs(753 - X))
    print(result)

=======
Suggestion 8

def main():
    S = input()
    print(min(abs(int(S[i:i+3])-753) for i in range(len(S)-2)))

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = 753 - int(s[:3])
    for i in range(n-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    min = 1000
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        if abs(X - 753) < min:
            min = abs(X - 753)
    print(min)
