Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    print(S.count('R'))

=======
Suggestion 2

def main():
    a = input()
    count = 0
    max_count = 0
    for i in range(3):
        if a[i] == "R":
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)
    print(max_count)

=======
Suggestion 3

def problem175_a():
    S = input()
    if S == "RRR":
        print(3)
    elif S == "RRS" or S == "SRR":
        print(2)
    elif S == "SSS":
        print(0)
    else:
        print(1)

=======
Suggestion 4

def main():
    s = input()
    r = s.count('R')
    print(r)

=======
Suggestion 5

def max_rain_days(s):
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

=======
Suggestion 6

def problem175_a(s):
    if s == 'RRR':
        return 3
    elif s == 'RRS' or s == 'SRR':
        return 2
    elif s == 'SSS':
        return 0
    else:
        return 1

=======
Suggestion 7

def main():
    s = input()
    print(s.count('R'))

=======
Suggestion 8

def main():
    s = input()
    a = s.count('R')
    print(a)

=======
Suggestion 9

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(0)
    elif S[0] == S[1] or S[1] == S[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 10

def main():
    S = input()
    print(S.count("R"))
