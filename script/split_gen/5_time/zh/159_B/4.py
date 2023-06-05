def is_palindrome(str):
    if len(str) <= 1:
        return True
    else:
        return str[0] == str[-1] and is_palindrome(str[1:-1])
