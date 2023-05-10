Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    s = ''.join(s)
    print(s)

=======
Suggestion 2

def main():
    s = input()
    a, b = map(int, input().split())
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    print(s)

=======
Suggestion 3

def swap(s, a, b):
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return s

=======
Suggestion 4

def main():
    s = input()
    a, b = map(int, input().split())
    print(s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:])

=======
Suggestion 5

def problem236a(s, a, b):
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return "".join(s)

=======
Suggestion 6

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

=======
Suggestion 7

def replace_char(str, i, j):
    str_list = list(str)
    tmp = str_list[i-1]
    str_list[i-1] = str_list[j-1]
    str_list[j-1] = tmp
    return ''.join(str_list)

=======
Suggestion 8

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
