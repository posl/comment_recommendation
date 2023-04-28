Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

=======
Suggestion 2

def main():
    s = input()
    a, b = map(int, input().split())

    print(s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])

=======
Suggestion 3

def swap_at(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

s = input()
a, b = map(int, input().split())
print(swap_at(s, a, b))

=======
Suggestion 4

def solve():
    s=input()
    a,b=map(int,input().split())
    print(s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:])

=======
Suggestion 5

def exchange_char(str, a, b):
    str_list = list(str)
    tmp = str_list[a-1]
    str_list[a-1] = str_list[b-1]
    str_list[b-1] = tmp
    return ''.join(str_list)

str = input()
a, b = map(int, input().split())
print(exchange_char(str, a, b))

=======
Suggestion 6

def swap_string(s, a, b):
    a = a - 1
    b = b - 1
    c = s[a]
    s[a] = s[b]
    s[b] = c
    return s

=======
Suggestion 7

def swap_char(string, a, b):
    string = list(string)
    string[a-1], string[b-1] = string[b-1], string[a-1]
    return ''.join(string)

=======
Suggestion 8

def replace_word(str, a, b):
    return str[:a-1] + str[b-1] + str[a:b-1] + str[a-1] + str[b:]
