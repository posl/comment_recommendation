Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 2

def problem():
    S = input()
    a, b = map(int, input().split())
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    return S

print(problem())

=======
Suggestion 3

def swap_char(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 4

def swap(string, a, b):
    if a > b:
        a, b = b, a
    return string[:a-1] + string[b-1] + string[a:b-1] + string[a-1] + string[b:]

=======
Suggestion 5

def swap(s, a, b):
    c = list(s)
    c[a-1], c[b-1] = c[b-1], c[a-1]
    return "".join(c)

s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

=======
Suggestion 6

def swap_char(s, a, b):
    s_list = list(s)
    s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]
    return ''.join(s_list)

s = input()
a, b = map(int, input().split())
print(swap_char(s, a, b))

=======
Suggestion 7

def swap_char(s,a,b):
    char_list = list(s)
    char_list[a-1], char_list[b-1] = char_list[b-1], char_list[a-1]
    return ''.join(char_list)

=======
Suggestion 8

def swap(input_string, a, b):
    a = a - 1
    b = b - 1
    input_string_list = list(input_string)
    tmp = input_string_list[a]
    input_string_list[a] = input_string_list[b]
    input_string_list[b] = tmp
    return "".join(input_string_list)

=======
Suggestion 9

def swap_string():
    string = input("Enter the String: ")
    a, b = map(int, input("Enter the values of a and b: ").split())
    a = a - 1
    b = b - 1
    string = list(string)
    string[a], string[b] = string[b], string[a]
    string = ''.join(string)
    print(string)

swap_string()
