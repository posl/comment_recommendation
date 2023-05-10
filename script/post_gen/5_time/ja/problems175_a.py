Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    S = input()
    # solve
    count = 0
    max = 0
    for i in S:
        if i == 'R':
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    # output
    print(max)

=======
Suggestion 2

def main():
    s = input()
    count = 0
    max_count = 0
    for i in s:
        if i == 'R':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 3

def main():
    s = input()
    l = 0
    r = 0
    for i in s:
        if i == 'R':
            r += 1
            l = 0
        else:
            l += 1
            r = 0
    print(max(r, l))

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(0)
    elif S[0] != S[1] != S[2] != S[0]:
        print(1)
    else:
        print(2)

=======
Suggestion 5

def main():
    S = input()
    S = S.replace('R',' ')
    S = S.split()
    print(len(S[0]))

=======
Suggestion 6

def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == "R":
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 7

def main():
    s = input()
    if s == "RRR":
        print(3)
    elif s == "RRS" or s == "SRR":
        print(2)
    elif s == "SSS":
        print(0)
    else:
        print(1)

=======
Suggestion 8

def main():
    s = input()
    r = s.replace('S', '0')
    r = r.replace('R', '1')
    r = r.replace('0', 'R')
    r = r.replace('1', 'S')
    print(r.count('R'))

=======
Suggestion 9

def main():
    s = input()
    s = s.split('R')
    print(max([len(i) for i in s]))

=======
Suggestion 10

def main():
    S = input()
    print(S.count('R'))
