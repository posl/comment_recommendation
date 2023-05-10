def is_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
n = input()

if __name__ == '__main__':
    is_palindrome()