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

def main():
    S = input()
    max_len = 0
    count = 0
    for s in S:
        if s in 'ACGT':
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 0
    print(max_len)

=======
Suggestion 3

def main():
    s = input()
    max_len = 0
    count = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            count += 1
        else:
            count = 0
        max_len = max(max_len, count)
    print(max_len)
main()

=======
Suggestion 4

def main():
    s = input()
    max_length = 0
    length = 0
    for c in s:
        if c in 'ACGT':
            length += 1
            max_length = max(max_length, length)
        else:
            length = 0
    print(max_length)

=======
Suggestion 5

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if all(c in 'ACGT' for c in s[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)

=======
Suggestion 6

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isACGT(s[i:j+1]):
                ans = max(ans, j-i+1)
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_acgt(s[i:j]):
                ans = max(ans, j-i)
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if (j-i) > max_len and check(s[i:j]):
                max_len = j-i
    print(max_len)

=======
Suggestion 10

def main():
    s = input()
    max_length = 0
    length = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            length += 1
        else:
            length = 0
        max_length = max(max_length, length)
    print(max_length)
