Synthesizing 10/10 solutions

=======
Suggestion 1

def find_missing_number(s):
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 2

def getMissingNumber(S):
    a = [0] * 10
    for i in S:
        a[int(i)] = 1
    for i in range(10):
        if a[i] == 0:
            return i

=======
Suggestion 3

def get_missing_number(str):
    for i in range(10):
        if str.find(str(i)) == -1:
            return i

=======
Suggestion 4

def problem248_a():
    s = input()
    s = list(s)
    s.sort()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

problem248_a()

=======
Suggestion 5

def main():
    s = input()
    for i in range(10):
        if not str(i) in s:
            print(i)
            break

=======
Suggestion 6

def missing_number(s):
    s = list(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 7

def missing_number(s):
    for i in range(0,10):
        if str(i) not in s:
            return i

=======
Suggestion 8

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    S.sort()
    for i in range(10):
        if i not in S:
            print(i)
            break

=======
Suggestion 9

def get_input():
    return input()

=======
Suggestion 10

def solution(s):
    for i in range(1,10):
        if str(i) not in s:
            print(i)
            break
