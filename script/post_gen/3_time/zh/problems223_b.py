Synthesizing 10/10 solutions

=======
Suggestion 1

def lexicographical_order(s):
    s = list(s)
    s.sort()
    return ''.join(s)

=======
Suggestion 2

def min_max(S):
    min = S
    max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min:
            min = S
        if S > max:
            max = S
    return min, max

=======
Suggestion 3

def getMinString(s):
    sLen = len(s)
    minStr = s
    for i in range(1, sLen):
        tmpStr = s[i:] + s[:i]
        if tmpStr < minStr:
            minStr = tmpStr
    return minStr

=======
Suggestion 4

def main():
    S = input()
    S = S[:1000]
    min = S
    max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min:
            min = S
        elif S > max:
            max = S
    print(min)
    print(max)

=======
Suggestion 5

def main():
    s = input()
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 6

def main():
    s = input()
    s = s.strip()
    s = s.lower()
    s = s + s
    s_min = s
    s_max = s
    for i in range(len(s)):
        if s[i:] + s[:i] < s_min:
            s_min = s[i:] + s[:i]
        if s[i:] + s[:i] > s_max:
            s_max = s[i:] + s[:i]
    print(s_min[0:len(s)//2])
    print(s_max[0:len(s)//2])

=======
Suggestion 7

def get_min_max(s):
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    return min_s,max_s

=======
Suggestion 8

def min_max(s):
    s = list(s)
    min_s = s[:]
    max_s = s[:]
    for i in range(len(s)):
        s.append(s.pop(0))
        if s < min_s:
            min_s = s[:]
        elif s > max_s:
            max_s = s[:]
    return ''.join(min_s), ''.join(max_s)

=======
Suggestion 9

def func(s):
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        min_s = min(min_s, s)
        max_s = max(max_s, s)
    return min_s, max_s

=======
Suggestion 10

def min_max(s):
    s = s+s
    min_s = s
    max_s = s
    for i in range(len(s)):
        if s[i:] + s[:i] < min_s:
            min_s = s[i:] + s[:i]
        if s[i:] + s[:i] > max_s:
            max_s = s[i:] + s[:i]
    return min_s[:len(s)//2], max_s[:len(s)//2]
