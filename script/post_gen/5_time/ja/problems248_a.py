Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(1, 10):
        if not str(i) in s:
            print(i)
            return

=======
Suggestion 2

def main():
    s = input()
    s = sorted(s)
    for i in range(0,10):
        if str(i) not in s:
            print(i)
            return

=======
Suggestion 3

def main():
    S = input()
    S = list(S)
    S = [int(i) for i in S]
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break

=======
Suggestion 4

def main():
    s = input()
    for i in range(1, 10):
        if not str(i) in s:
            print(i)
            break

=======
Suggestion 5

def main():
    s = input()
    s = list(s)
    s.sort()
    if s[0] == '1':
        print(2)
    else:
        print(1)

=======
Suggestion 6

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 7

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            exit()
