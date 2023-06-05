def is_palindrome(str):
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return is_palindrome(str[1:-1])
    else:
        return False
