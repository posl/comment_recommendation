def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
S = input()
N = len(S)

if __name__ == '__main__':
    is_palindrome()