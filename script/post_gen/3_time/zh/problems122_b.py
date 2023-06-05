Synthesizing 10/10 solutions

=======
Suggestion 1

def check(s):
    if s == "A" or s == "C" or s == "G" or s == "T":
        return True
    else:
        return False

=======
Suggestion 2

def problem122_b():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "T" or s[i] == "G" or s[i] == "C":
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
problem122_b()

=======
Suggestion 3

def find_max_length_of_acgt(s):
    length = 0
    max_length = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            length += 1
            if length > max_length:
                max_length = length
        else:
            length = 0
    return max_length

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    max_length = 0
    length = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            length += 1
        else:
            max_length = max(max_length, length)
            length = 0
    max_length = max(max_length, length)
    print(max_length)

=======
Suggestion 5

def main():
    S = input()
    max_length = 0
    for i in range(len(S)):
        length = 0
        for j in range(i, len(S)):
            if S[j] in 'ACGT':
                length += 1
            else:
                break
        if max_length < length:
            max_length = length
    print(max_length)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            ok = True
            for k in range(i,j+1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans,j-i+1)
    print(ans)

=======
Suggestion 7

def main():
    # input
    S = input()
    # compute
    res = 0
    count = 0
    for i in range(len(S)):
        if S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T':
            count += 1
        else:
            count = 0
        res = max(res, count)
    # output
    print(res)

=======
Suggestion 8

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                max_len = max(max_len, j-i+1)
    print(max_len)

=======
Suggestion 9

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
