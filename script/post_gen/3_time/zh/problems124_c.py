Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(min(s.count('0'),s.count('1'))*2)

=======
Suggestion 2

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '0':
                count += 1
        else:
            if s[i] == '1':
                count += 1
    print(min(count,len(s)-count))
main()

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if i == 0:
            if S[i] == S[i+1]:
                count += 1
        elif i == N-1:
            if S[i] == S[i-1]:
                count += 1
        else:
            if S[i] == S[i-1] or S[i] == S[i+1]:
                count += 1
    print(count)

=======
Suggestion 4

def solve():
    s = input()
    # 从左到右的颜色
    left = [0] * (len(s) + 1)
    # 从右到左的颜色
    right = [0] * (len(s) + 1)
    for i in range(len(s)):
        left[i + 1] = left[i] + int(s[i])
        right[i + 1] = right[i] + int(s[len(s) - i - 1])
    res = len(s)
    for i in range(len(s) + 1):
        res = min(res, left[i] + right[len(s) - i])
    print(res)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == '1':
            count += 1
        elif i % 2 == 1 and s[i] == '0':
            count += 1
    print(min(count, len(s) - count))

=======
Suggestion 6

def solve(s):
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s[0] == s[1]:
        return 1 + solve(s[1:])
    else:
        return solve(s[1:])

=======
Suggestion 7

def min_flip(s):
    # 从左到右遍历，如果遇到与前一个相同的，就要翻转
    n = len(s)
    cnt = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
    return cnt

=======
Suggestion 8

def main():
    s = input()
    b = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "0":
            b += 1
        else:
            w += 1
    print(min(b, w) * 2)

=======
Suggestion 9

def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        if i%2 == 0 and s[i] == '0':
            count += 1
        if i%2 == 1 and s[i] == '1':
            count += 1
    print(min(count,len(s)-count))
