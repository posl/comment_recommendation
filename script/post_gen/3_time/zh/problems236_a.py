Synthesizing 10/10 solutions

=======
Suggestion 1

def swap_char(string, a, b):
    # print(string, a, b)
    l = list(string)
    l[a-1], l[b-1] = l[b-1], l[a-1]
    return "".join(l)

=======
Suggestion 2

def main():
    s = input()
    a,b = map(int,input().split())
    print(s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:])

=======
Suggestion 3

def swap(str, a, b):
    str_list = list(str)
    str_list[a-1], str_list[b-1] = str_list[b-1], str_list[a-1]
    return ''.join(str_list)

=======
Suggestion 4

def change(a,b,s):
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    return "".join(s)

=======
Suggestion 5

def swap_char(string, a, b):
    if a > b:
        a, b = b, a
    return string[:a-1] + string[b-1] + string[a:b-1] + string[a-1] + string[b:]

=======
Suggestion 6

def main():
    s = input()
    a, b = map(int, input().split())
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    print(''.join(s))

=======
Suggestion 7

def main():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 8

def solve():
    s = input()
    a, b = map(int, input().split())
    print(s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])

=======
Suggestion 9

def swap(s,a,b):
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    return s

=======
Suggestion 10

def swap_char(s, a, b):
    s = list(s)
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return ''.join(s)
