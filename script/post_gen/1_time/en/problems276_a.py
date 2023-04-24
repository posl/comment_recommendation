Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s.find('a') == -1:
        print(-1)
    else:
        print(s.rfind('a') + 1)

=======
Suggestion 2

def find_last_occurence(string, char):
    index = -1
    for i in range(len(string)):
        if string[i] == char:
            index = i + 1
    return index

string = input()
char = 'a'
print(find_last_occurence(string, char))

=======
Suggestion 3

def find_last_occurrence(str, ch):
    for i in range(len(str)-1, -1, -1):
        if str[i] == ch:
            return i + 1
    return -1

=======
Suggestion 4

def solve():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a')+1)
    return 0

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a')+1)

=======
Suggestion 6

def main():
    s = input()
    a = s.rfind('a')
    print(a+1)

=======
Suggestion 7

def main():
    input_string = input()
    print(input_string.rfind('a') + 1)

=======
Suggestion 8

def last_index(s, c):
    return len(s) - s[::-1].index(c)

=======
Suggestion 9

def get_input():
    return input()
