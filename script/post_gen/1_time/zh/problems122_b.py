Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    max_len = 0
    count = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    print(max_len)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isACGT(s[i:j+1]):
                ans = max(ans, j-i+1)
    print(ans)

=======
Suggestion 3

def solution():
    s = input()
    n = len(s)
    max = 0
    for i in range(n):
        for j in range(i, n):
            if check(s[i:j + 1]):
                if max < j - i + 1:
                    max = j - i + 1
    print(max)

=======
Suggestion 4

def solve():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if is_acgt(sub):
                max_len = max(max_len, len(sub))
    print(max_len)

=======
Suggestion 5

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                max_len = max(max_len, j-i+1)
    print(max_len)

=======
Suggestion 6

def main():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s in ['A', 'C', 'G', 'T']:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    max_length = 0
    length = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            length += 1
        else:
            length = 0
        if length > max_length:
            max_length = length
    print(max_length)

=======
Suggestion 8

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_ACGT(s[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)

=======
Suggestion 9

def getStrLen(str):
    maxLen = 0
    count = 0
    for i in range(len(str)):
        if str[i] == 'A' or str[i] == 'C' or str[i] == 'G' or str[i] == 'T':
            count += 1
            if count > maxLen:
                maxLen = count
        else:
            count = 0
    return maxLen

str = input()
print(getStrLen(str))

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ok = True
            for k in range(i, j + 1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans, j - i + 1)
    print(ans)
