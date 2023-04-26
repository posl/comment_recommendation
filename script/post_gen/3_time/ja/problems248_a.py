Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 2

def main():
    s = input()
    for i in range(1, 10):
        if str(i) not in s:
            print(i)
            exit()

=======
Suggestion 3

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

=======
Suggestion 4

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            return

=======
Suggestion 5

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    for i in range(1, 10):
        if i not in S:
            print(i)
            break

=======
Suggestion 6

def main():
    S = input()
    S = list(map(int, S))
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break

=======
Suggestion 7

def main():
    S = input()
    S = list(S)
    S = list(map(int,S))
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break

=======
Suggestion 8

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))

    for i in range(10):
        if i not in S:
            print(i)
            exit()

=======
Suggestion 9

def main():
    S = input()
    S = sorted(S)
    if S[0] == '1':
        print('2')
    else:
        print('1')

=======
Suggestion 10

def main():
    s = input()
    print(45 - sum([int(i) for i in s]))
