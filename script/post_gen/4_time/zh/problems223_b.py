Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate_left(s):
    l = list(s)
    first = l.pop(0)
    l.append(first)
    return ''.join(l)

=======
Suggestion 2

def main():
    s = input()
    l = len(s)
    min = s
    max = s
    for i in range(1, l):
        s = s[1:] + s[0]
        if s < min:
            min = s
        if s > max:
            max = s
    print(min)
    print(max)

=======
Suggestion 3

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
Suggestion 4

def minstr(s):
    s = list(s)
    a = min(s)
    b = s.index(a)
    c = s[:b]
    del s[:b]
    s.extend(c)
    return ''.join(s)

=======
Suggestion 5

def main():
    s = input()
    length = len(s)
    min_s = s
    max_s = s
    for i in range(1,length):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        elif s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

=======
Suggestion 6

def main():
    s = input()
    a = [s]
    for i in range(len(s)):
        s = s[1:]+s[0]
        a.append(s)
    print(min(a))
    print(max(a))

=======
Suggestion 7

def main():
    s = input()
    l = len(s)
    s = s + s
    s_min = s[0:l]
    s_max = s[0:l]
    for i in range(1, l):
        s_min = min(s_min, s[i:i+l])
        s_max = max(s_max, s[i:i+l])
    print(s_min)
    print(s_max)

=======
Suggestion 8

def rotate(s):
    return s[1:] + s[0]

=======
Suggestion 9

def solve():
    S = input()
    S1 = S
    S2 = S
    for i in range(len(S)):
        S1 = S1[1:] + S1[0]
        S2 = S2[-1] + S2[0:-1]
        if S1 < S2:
            print(S1)
            print(S2)
            break
        elif S1 > S2:
            print(S2)
            print(S1)
            break
        else:
            continue
solve()

=======
Suggestion 10

def main():
    s = input()
    s = s * 2
    s_min = s[0:len(s)//2]
    s_max = s[0:len(s)//2]
    for i in range(1,len(s)//2):
        s_min = min(s_min,s[i:i+len(s)//2])
        s_max = max(s_max,s[i:i+len(s)//2])
    print(s_min)
    print(s_max)
