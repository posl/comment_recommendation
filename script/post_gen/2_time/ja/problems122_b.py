Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    s = s.replace('A', '1')
    s = s.replace('C', '2')
    s = s.replace('G', '3')
    s = s.replace('T', '4')
    s = s.replace('1', 'A')
    s = s.replace('2', 'C')
    s = s.replace('3', 'G')
    s = s.replace('4', 'T')
    s = s.split('A')
    s = s.split('C')
    s = s.split('G')
    s = s.split('T')
    s = s.split('AC')
    s = s.split('AG')
    s = s.split('AT')
    s = s.split('CG')
    s = s.split('CT')
    s = s.split('GT')
    s = s.split('ACG')
    s = s.split('ACT')
    s = s.split('AGT')
    s = s.split('CGT'

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
        else:
            if count > ans:
                ans = count
            count = 0
    if count > ans:
        ans = count
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 6

def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 7

def main():
    s = input()
    s = s.replace('A', 'a')
    s = s.replace('C', 'c')
    s = s.replace('G', 'g')
    s = s.replace('T', 't')
    s = s.split('a')
    s = s.split('c')
    s = s.split('g')
    s = s.split('t')
    print(s)

main()

=======
Suggestion 8

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] in "ACGT":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    dp = [0] * n
    for i in range(n):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            if i == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    print(max(dp))

=======
Suggestion 10

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if all(c in "ACGT" for c in s[i:j + 1]):
                ans = max(ans, j - i + 1)
    print(ans)

main()
