Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def isHuiwen(str):
    length = len(str)
    for i in range(length/2):
        if str[i] != str[length-1-i]:
            return False
    return True

=======
Suggestion 2

def is_palindrome(num):
    return str(num) == str(num)[::-1]

=======
Suggestion 3

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 4

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

=======
Suggestion 5

def is_huiwen(number):
    number = str(number)
    for i in range(len(number)):
        if number[i] != number[-(i+1)]:
            return False
    return True

=======
Suggestion 6

def is_palindrome(s):
    if len(s) == 1:
        return True
    else:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True

=======
Suggestion 7

def is_palindrome(num):
    num_str = str(num)
    num_str_len = len(num_str)
    if num_str_len == 1:
        return True
    elif num_str_len == 2:
        return True if num_str[0] == num_str[1] else False
    else:
        if num_str[0] == num_str[num_str_len - 1]:
            return is_palindrome(num_str[1:num_str_len - 1])
        else:
            return False

=======
Suggestion 8

def isPalindrome(s):
    return s == s[::-1]
