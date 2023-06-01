Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    n = len(s) - 1
    an

=======
Suggestion 2

def main():
    S = input()
    S = int(S)
    count = 0
    while S > 0:
        if S % 100 == 0:
            S = S // 100
        else:
            S = S - S % 10
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != '0':
            ans += 1
    if s[-1] != '0':
        print(ans)
    else:
        print(ans-1)

=======
Suggestion 4

def main():
    S = input()
    if S == '0':
        print(0)
        return
    ans = 10000000
    for i in range(1, 11):
        if i == 1:
            dp = [0] * len(S)
            if S[0] != '1':
                dp[0] = 1
        else:
            dp = [10000000] * len(S)
            if S[0] != '1':
                dp[0] = 2
            else:
                dp[0] = 1
        for j in range(1, len(S)):
            if S[j] == '0':
                dp[j] = dp[j - 1] + 1
            else:
                if dp[j - 1] == 10000000:
                    dp[j] = 10000000
                else:
                    dp[j] = min(dp[j], dp[j - 1] + i)
            if j == len(S) - 1:
                if S[j] == '1':
                    ans = min(ans, dp[j])
                else:
                    ans = min(ans, dp[j] + 1)
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    S = input()
    S = int(S)
    count = 0
    while S > 0:
        if S % 10 == 0:
            S //= 10
            count += 1
        else:
            S -= 1
            count += 1
    print(count)

=======
Suggestion 7

def main():
    s = input()
    s_len = len(s)
    count = 0
    index = 0
    while index < s_len:
        if index == 0 and s[index] == '1':
            index += 1
            continue
        if s[index] == '0':
            index += 1
            count += 1
            continue
        if s[index] == '1':
            if index == s_len - 1:
                count += 1
                break
            if s[index + 1] == '0':
                index += 1
                count += 1
                continue
        count += 1
        index += 1
    print(count)

=======
Suggestion 8

def main():
    s = input()
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        if i == 0:
            ans += int(s[i])
        elif i == 1:
            ans += int(s[i]) * 2
        else:
            ans += int(s[i]) * (i + 1)
    print(ans)

=======
Suggestion 9

def solve(s):
    s = list(s)
    s.reverse()
    i = 0
    count = 0
    while i < len(s):
        if s[i] == '0':
            i += 1
            count += 1
        else:
            j = i
            while j < len(s):
                if s[j] == '0':
                    break
                j += 1
            if j == len(s):
                break
            else:
                count += 1
                i = j
    return count
