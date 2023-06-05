def is_palindrome(n):
    n = str(n)
    #print(n)
    if n == n[::-1]:
        return True
    else:
        return False
