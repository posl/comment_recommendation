Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s in 'ACGT':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    ans = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] in "ACGT":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    max_count = 0
    for i in s:
        if i in 'ACGT':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    print(max_count)

=======
Suggestion 6

def countACGT(s):
    count = 0
    for i in s:
        if i in 'ACGT':
            count += 1
        else:
            break
    return count

=======
Suggestion 7

def longest_ACGT(s):
    a = 0
    b = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            a += 1
        else:
            if a > b:
                b = a
            a = 0
    if a > b:
        b = a
    return b

s = input()
print(longest_ACGT(s))

I have a list of strings, and I want to find the longest string that is a substring of another string. For example, if I have the list of strings ["ATC", "ATAGA", "TCO"] and the string "ATCODER", then I want to find the longest string in the list that is a substring of the string "ATCODER", which is "ATC". I can write a function that takes in a list of strings and a string and returns the longest string in the list that is a substring of the string, but I can't figure out how to make it so that I can call this function without passing in the list of strings every time. For example, I want to be able to call the function like this:

longest_ACGT("ATCODER")

and have it return "ATC". I'm not sure how to do this. I've tried using a global variable to store the list of strings, but I can't figure out how to make it so that I can call the function without passing in the list of strings every time.

Here is my code so far:

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j + 1].count("A") * s[i:j + 1].count("C") * s[i:j + 1].count("G") * s[i:j + 1].count("T") != 0:
                ans = max(ans, j - i + 1)
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            t = s[i:j+1]
            if not 'ACGT' in t:
                break
            ans = max(ans, len(t))
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    ACGT = 'ACGT'
    #print(S)
    #print(ACGT)
    max = 0
    count = 0
    for i in range(len(S)):
        #print(i)
        if S[i] in ACGT:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
