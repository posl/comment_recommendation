Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 753
    for i in range(len(s)-2):
        ans = min(ans, abs(753-int(s[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 1000
    for i in range(len(S) - 2):
        ans = min(ans, abs(753 - int(S[i:i + 3])))
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = 10**10
    for i in range(len(s)-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    ans = 10**9

    for i in range(len(S)-2):
        X = int(S[i:i+3])
        ans = min(ans, abs(X-753))

    print(ans)

=======
Suggestion 5

def main():
    S = input()
    ans = 753

    for i in range(len(S)-2):
        ans = min(ans, abs(753-int(S[i:i+3])))

    print(ans)

=======
Suggestion 6

def main():
    s = input()
    l = len(s)
    ans = 10**10
    for i in range(l-2):
        x = int(s[i:i+3])
        ans = min(ans, abs(x-753))
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    min = 1000
    for i in range(3, len(S) + 1):
        x = int(S[i - 3:i])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)

=======
Suggestion 8

def main():
    S = input()
    num = 753
    diff = 1000
    for i in range(len(S)-2):
        if diff > abs(num - int(S[i:i+3])):
            diff = abs(num - int(S[i:i+3]))
    print(diff)

=======
Suggestion 9

def main():
    S = input()
    S = [int(s) for s in S]
    ans = 10**10
    for i in range(len(S) - 2):
        ans = min(ans, abs(753 - (S[i] * 100 + S[i + 1] * 10 + S[i + 2])))
    print(ans)

=======
Suggestion 10

def main():
    # 入力
    s = input()
    # 753 との差の最小値を求める
    ans = 10 ** 9
    for i in range(len(s) - 2):
        x = int(s[i:i + 3])
        ans = min(ans, abs(x - 753))
    # 出力
    print(ans)
