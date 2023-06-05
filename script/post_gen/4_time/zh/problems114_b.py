Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = [int(i) for i in S]
    min_diff = 1000
    for i in range(len(S)-2):
        num = S[i]*100 + S[i+1]*10 + S[i+2]
        min_diff = min(min_diff, abs(num - 753))
    print(min_diff)

=======
Suggestion 2

def main():
    S = input()
    X = []
    for i in range(len(S)-2):
        X.append(abs(753-int(S[i:i+3])))
    print(min(X))

=======
Suggestion 3

def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        x = int(S[i:i+3])
        if abs(x-753) < min_diff:
            min_diff = abs(x-753)
    print(min_diff)

=======
Suggestion 4

def main():
    s = input()
    min_diff = 1000
    for i in range(len(s)-2):
        diff = abs(int(s[i:i+3])-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 5

def main():
    s = input()
    min_diff = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    S = input()
    ans = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        ans = min(ans, abs(753-X))
    print(ans)

=======
Suggestion 7

def diff(n):
    return abs(753-n)

=======
Suggestion 8

def main():
    S = input()
    print(min(abs(int(S[i:i+3])-753) for i in range(len(S)-2)))

=======
Suggestion 9

def main():
    # 读入数据
    S = input()
    # 计算结果
    min = 1000
    for i in range(0, len(S) - 2):
        X = int(S[i:i + 3])
        if abs(X - 753) < min:
            min = abs(X - 753)
    # 输出结果
    print(min)

=======
Suggestion 10

def main():
    S = input()
    S = list(S)
    S = [int(x) for x in S]
    min = 753
    for i in range(len(S)-2):
        X = int(S[i])*100 + int(S[i+1])*10 + int(S[i+2])
        if abs(X-753) < min:
            min = abs(X-753)
    print(min)
