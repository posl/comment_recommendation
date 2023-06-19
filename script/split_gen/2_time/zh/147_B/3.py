def check_palindrome(str):
    length = len(str)
    for i in range(0, length//2):
        if str[i] != str[length-1-i]:
            return False
    return True
