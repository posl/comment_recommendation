Synthesizing 10/10 solutions

=======
Suggestion 1

def problem242_b():
    S = input()
    print(''.join(sorted(S)))

=======
Suggestion 2

def main():
    s = input()
    s = sorted(s)
    print(''.join(s))

=======
Suggestion 3

def main():
    s = input()
    print(min(s[i:] + s[:i] for i in range(len(s))))

=======
Suggestion 4

def problem242_b():
    S = input()
    S = sorted(S)
    print(''.join(S))

=======
Suggestion 5

def main():
    S = input()
    l = list(S)
    l.sort()
    print(''.join(l))

=======
Suggestion 6

def solve():
    s = list(input())
    s.sort()
    print(''.join(s))

=======
Suggestion 7

def main():
    s = input()
    l = list(s)
    l.sort()
    print(''.join(l))

=======
Suggestion 8

def main():
    a = input()
    b = sorted(a)
    print("".join(b))

=======
Suggestion 9

def problem242_b():
    string = input()
    list = []
    for i in range(len(string)):
        list.append(string[i])
    list.sort()
    for i in range(len(list)):
        print(list[i],end = "")
    print()

=======
Suggestion 10

def main():
    s = input()
    s = list(s)
    s.sort()
    print(''.join(s))
