def is_palindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True
