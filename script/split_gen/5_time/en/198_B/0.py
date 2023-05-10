def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False
