Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    print(max)

=======
Suggestion 3

def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 4

def solve():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s == 'A' or s == 'C' or s == 'G' or s == 'T':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)
    return 0

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    max_len = 0
    cur_len = 0
    for c in s:
        if c in "ACGT":
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
    print(max_len)

=======
Suggestion 7

def main():
    s = input()
    max_length = 0
    current_length = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            current_length += 1
        else:
            current_length = 0
        max_length = max(max_length, current_length)
    print(max_length)

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if not 'A' in s[i:j+1] and not 'C' in s[i:j+1] and not 'G' in s[i:j+1] and not 'T' in s[i:j+1]:
                ans = max(ans, j-i+1)
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if all(c in 'ATGC' for c in s[i:j+1]):
                ans = max(ans, j-i+1)
    print(ans)
main()

=======
Suggestion 10

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if set(s[i:j]) <= set('ACGT'):
                ans = max(ans, j - i)
    print(ans)
