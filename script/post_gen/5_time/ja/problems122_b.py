Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    ans = 0
    cnt = 0
    for c in s:
        if c in 'ACGT':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

=======
Suggestion 2

def count_acgt(str):
    count = 0
    max_count = 0
    for i in range(len(str)):
        if str[i] == "A" or str[i] == "C" or str[i] == "G" or str[i] == "T":
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count

=======
Suggestion 3

def main():
    s = input()
    max = 0
    tmp = 0
    for c in s:
        if c in ['A', 'C', 'G', 'T']:
            tmp += 1
            if tmp > max:
                max = tmp
        else:
            tmp = 0
    print(max)

=======
Suggestion 4

def solve():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] in ["A","C","G","T"]:
            count += 1
            ans = max(ans,count)
        else:
            count = 0
    print(ans)

=======
Suggestion 6

def main():
    # input
    S = input()
    # compute
    max_len = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if is_ATGC(S[i:j+1]):
                max_len = max(max_len, j-i+1)
    # output
    print(max_len)

=======
Suggestion 7

def main():
    s = input()
    s = s.replace("A", "1")
    s = s.replace("T", "1")
    s = s.replace("C", "1")
    s = s.replace("G", "1")
    s = s.replace("1", " ")
    s = s.split()
    print(len(max(s, key=len)))

=======
Suggestion 8

def main():
    s = input()
    t = ""
    max_len = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            t += s[i]
            max_len = max(max_len, len(t))
        else:
            t = ""
    print(max_len)

=======
Suggestion 9

def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 10

def main():
    S = input()
    max_count = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0

    print(max_count)
