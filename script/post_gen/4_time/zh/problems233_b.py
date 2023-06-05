Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse_string(str, l, r):
    return str[:l-1] + str[l-1:r][::-1] + str[r:]

=======
Suggestion 2

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 3

def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, (l+r)/2):
        tmp = s[i]
        s[i] = s[r-i+l-1]
        s[r-i+l-1] = tmp
    return ''.join(s)

=======
Suggestion 4

def reverse_string(string, start, end):
    string_list = list(string)
    string_list[start:end+1] = reversed(string_list[start:end+1])
    return ''.join(string_list)

=======
Suggestion 5

def reverse(l, r, s):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 6

def reverse_string(s, l, r):
    if l == 1:
        return s[r-1::-1] + s[r:]
    else:
        return s[:l-1] + s[r-1:l-2:-1] + s[r:]

=======
Suggestion 7

def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    return ''.join(s)

=======
Suggestion 8

def reverse(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 9

def reverse_str(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

=======
Suggestion 10

def reverse_string(string, begin, end):
    """
    :param string: string to be reversed
    :param begin: begin index
    :param end: end index
    :return: reversed string
    """
    if begin >= end:
        return string
    else:
        string = string[:begin] + string[end] + string[begin + 1:end] + string[begin] + string[end + 1:]
        return reverse_string(string, begin + 1, end - 1)
