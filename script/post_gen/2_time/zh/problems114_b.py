Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    min_diff = 999
    for i in range(0, len(S)-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 2

def main():
    s=input()
    n=len(s)
    ans=10**9
    for i in range(n-2):
        x=int(s[i:i+3])
        ans=min(ans,abs(x-753))
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    s = list(map(int, s))
    ans = 1000
    for i in range(len(s)-2):
        x = s[i]*100 + s[i+1]*10 + s[i+2]
        ans = min(ans, abs(x-753))
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    ans = 10**9
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        ans = min(ans,abs(753-X))
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    print(min(abs(int(S[i:i+3])-753) for i in range(len(S)-2)))

=======
Suggestion 6

def main():
    S = input()
    l = len(S)
    diff = 1000
    for i in range(l-2):
        X = int(S[i:i+3])
        if abs(X-753) < diff:
            diff = abs(X-753)
    print(diff)

=======
Suggestion 7

def main():
    S = input()
    min_diff = 753
    for i in range(len(S)-2):
        diff = abs(int(S[i:i+3]) - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    # 读取输入
    S = input()
    # 求解并输出
    print(solve(S))

=======
Suggestion 9

def main():
    S = input()
    min_diff = 1000
    for i in range(0, len(S)-2):
        diff = abs(int(S[i:i+3])-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 10

def get_min_diff(S):
    min_diff = 999
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        min_diff = min(min_diff, abs(X-753))
    return min_diff
