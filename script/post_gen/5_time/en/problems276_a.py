Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if "a" in s:
        print(s.rfind("a") + 1)
    else:
        print(-1)

=======
Suggestion 2

def main():
    S = input()
    if S.find('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 3

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 4

def main():
    s = input()
    if s.find('a') >= 0:
        print(s.rfind('a')+1)
    else:
        print(-1)

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 6

def main():
    S = input()
    print(S.rfind('a')+1)

=======
Suggestion 7

def problem276_a():
    s = input()
    a = s.rfind('a')
    print(a+1)

problem276_a()

=======
Suggestion 8

def find_last_index_of_a(string):
    string_length = len(string)
    if string_length < 1 or string_length > 100:
        return -1
    for i in range(string_length, 0, -1):
        if string[i-1] == 'a':
            return i
    return -1

=======
Suggestion 9

def solve():
    S = input()
    print(S.rfind("a") + 1)
