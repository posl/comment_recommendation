Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 2

def main():
    s = input()
    max_len = 0
    cur_len = 0
    for c in s:
        if c in 'ACGT':
            cur_len += 1
        else:
            cur_len = 0
        if cur_len > max_len:
            max_len = cur_len
    print(max_len)

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s in "ACGT":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    max = 0
    count = 0
    for i in S:
        if i == "A" or i == "C" or i == "G" or i == "T":
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] in ['A', 'C', 'G', 'T']:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_acgt(s[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)

=======
Suggestion 7

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if 'A' not in s[i:j+1] and 'C' not in s[i:j+1] and 'G' not in s[i:j+1] and 'T' not in s[i:j+1]:
                break
            else:
                max_len = max(max_len, j - i + 1)
    print(max_len)

=======
Suggestion 8

def longest_acgt(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                longest = max(longest, j-i+1)
    return longest

=======
Suggestion 9

def solve():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if all(c in 'ACGT' for c in s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)

=======
Suggestion 10

def main():
    s = input()
    
    result = 0
    temp = 0
    for i in range(len(s)):
        if s[i] in ['A', 'T', 'C', 'G']:
            temp += 1
        else:
            temp = 0
        result = max(result, temp)
    
    print(result)
