Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = list(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 2

def find_miss_num(s):
    numbers = list(range(10))
    for i in range(len(s)):
        numbers.remove(int(s[i]))
    return numbers[0]

=======
Suggestion 3

def solve():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 4

def find_missing_number(s):
    number_list = []
    for i in range(0,10):
        number_list.append(str(i))
    for i in s:
        if i in number_list:
            number_list.remove(i)
    return number_list[0]

=======
Suggestion 5

def main():
    str = input()
    for i in range(1,10):
        if str.find(str(i)) == -1:
            print(i)
            break

=======
Suggestion 6

def main():
    s = input()
    s = list(s)
    s = list(map(int, s))
    s.sort()
    for i in range(1, 10):
        if i not in s:
            print(i)
            break

=======
Suggestion 7

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 8

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

=======
Suggestion 9

def main():
    s = input()
    s = list(s)
    for i in range(0,10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 10

def solution(S):
    for i in range(10):
        if str(i) not in S:
            print(i)
            break
