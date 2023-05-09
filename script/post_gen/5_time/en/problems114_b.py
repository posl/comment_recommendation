Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 999
    for i in range(len(s)-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = 753
    for i in range(N-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    ans = 10**9
    for i in range(len(S)-2):
        ans = min(ans,abs(753-int(S[i:i+3])))
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    print(min(abs(int(s[i:i+3]) - 753) for i in range(len(s) - 2)))

=======
Suggestion 5

def main():
    S = input()
    S = list(map(int, S))
    ans = 1000
    for i in range(len(S)-2):
        tmp = S[i]*100 + S[i+1]*10 + S[i+2]
        ans = min(ans, abs(753-tmp))
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    l = len(s)
    min = 999
    for i in range(l-2):
        x = int(s[i:i+3])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)

=======
Suggestion 7

def main():
    # Take input Here and Call solution function
    S = input()
    print(solution(S))

=======
Suggestion 8

def main():
    s = input()
    x = int(s)
    min = 10**10
    for i in range(0, len(s)-2):
        t = int(s[i:i+3])
        if abs(t-753) < min:
            min = abs(t-753)
    print(min)

=======
Suggestion 9

def get_input():
    return input()
