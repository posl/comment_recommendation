Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #s = input()
    s = "ATCODER"
    #s = "HATAGAYA"
    #s = "SHINJUKU"
    #s = "AC

=======
Suggestion 2

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)

=======
Suggestion 3

def get_longest_acgt(s):
    acgt_list = []
    acgt_str = ''
    for i in range(len(s)):
        if s[i] in 'ACGT':
            acgt_str += s[i]
        else:
            if acgt_str != '':
                acgt_list.append(acgt_str)
                acgt_str = ''
    if acgt_str != '':
        acgt_list.append(acgt_str)
        acgt_str = ''
    return len(max(acgt_list, key=len))

=======
Suggestion 4

def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 5

def main():
    S = input()
    max_len = 0
    len_S = len(S)
    for i in range(len_S):
        for j in range(i, len_S):
            if is_acgt(S[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)

=======
Suggestion 6

def main():
    s = input()
    res = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
    print(res)

=======
Suggestion 7

def main():
    S = input()
    max_len = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            if S[i:j].isalpha():
                if S[i:j].count('A') + S[i:j].count('C') + S[i:j].count('G') + S[i:j].count('T') == len(S[i:j]):
                    max_len = max(max_len,len(S[i:j]))
    print(max_len)

=======
Suggestion 8

def solve():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ok = True
            for k in range(i, j+1):
                if s[k] != "A" and s[k] != "C" and s[k] != "G" and s[k] != "T":
                    ok = False
            if ok:
                ans = max(ans, j-i+1)
    print(ans)

=======
Suggestion 9

def problem122_b(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isACGT(s[i:j]):
                max_len = max(max_len,j-i)
    return max_len

=======
Suggestion 10

def main():
    s = input()
    temp = 0
    max = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            temp += 1
            if max < temp:
                max = temp
        else:
            temp = 0
    print(max)
