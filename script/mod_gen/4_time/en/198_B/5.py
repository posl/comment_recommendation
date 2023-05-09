def is_palindrome(n):
    n_str = str(n)
    n_str_rev = n_str[::-1]
    return n_str == n_str_rev

if __name__ == '__main__':
    is_palindrome()