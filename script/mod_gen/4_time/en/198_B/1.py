def is_palindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False
    return True

if __name__ == '__main__':
    is_palindrome()