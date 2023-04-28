Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

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
Suggestion 3

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

=======
Suggestion 4

def check(c):
    if c == "A" or c == "C" or c == "G" or c == "T":
        return True
    else:
        return False

=======
Suggestion 5

def main():
    str = input()
    max = 0
    count = 0
    for i in range(len(str)):
        if str[i] == "A" or str[i] == "C" or str[i] == "G" or str[i] == "T":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 6

def count_acgt(s):
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count


s = input()
print(count_acgt(s))

=======
Suggestion 7

def main():
    s = input()
    max_len = 0
    tmp_len = 0
    for c in s:
        if c in "ACGT":
            tmp_len += 1
        else:
            tmp_len = 0
        max_len = max(max_len, tmp_len)
    print(max_len)

=======
Suggestion 8

def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i in ['A', 'C', 'G', 'T']:
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    print(max)

=======
Suggestion 9

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            flag = True
            for k in range(i,j+1):
                if s[k] != "A" and s[k] != "C" and s[k] != "G" and s[k] != "T":
                    flag = False
            if flag:
                ans = max(ans,j-i+1)
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    max_len = 0
    temp_len = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            temp_len += 1
        else:
            temp_len = 0
        max_len = max(max_len, temp_len)
    print(max_len)
