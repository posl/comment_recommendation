Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

main()

=======
Suggestion 2

def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

=======
Suggestion 3

def main():
    S = input()
    print(min(S.count("0"), S.count("1")) * 2)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if s[i] == "0":
            a[i] = 1
        else:
            b[i] = 1
    for i in range(1, n):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] + b[n - 1] - b[i])
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    B = 0
    for s in S:
        if s == '1':
            B += 1
    R = N - B
    ans = min(B, R) * 2
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    # 0の数と1の数をカウント
    # 0の数と1の数の小さい方が答え
    print(min(S.count('0'), S.count('1')) * 2)
