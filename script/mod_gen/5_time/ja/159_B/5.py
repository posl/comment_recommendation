def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
s = input()
l = len(s)

if __name__ == '__main__':
    is_palindrome()