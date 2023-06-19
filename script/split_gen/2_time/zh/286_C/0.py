def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return isPalindrome(str[1:-1])
