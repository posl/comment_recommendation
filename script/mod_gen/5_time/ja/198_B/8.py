def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True
N = input()

if __name__ == '__main__':
    is_palindrome()