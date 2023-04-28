Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '1':
            count += 1
        elif i % 2 == 1 and S[i] == '0':
            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == "1":
            count += 1
        elif i % 2 == 1 and S[i] == "0":
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] == '0':
                count += 1
        else:
            if S[i] == '1':
                count += 1
    print(count)

=======
Suggestion 4

def main():
    S = input()
    cnt = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '0':
            cnt += 1
        elif i % 2 == 1 and S[i] == '1':
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    S = input()
    c = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':
                c += 1
        else:
            if S[i] == '1':
                c += 1
    print(min(c, len(S) - c))

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        if i%2 == 0:
            if s[i] == '1':
                count += 1
        else:
            if s[i] == '0':
                count += 1
    print(count)

=======
Suggestion 7

def main():
    S = input()
    print(min(S.count('01'), S.count('10')) * 2)

=======
Suggestion 8

def main():
    s = input()
    print(min(s.count("01"), s.count("10")) * 2)
