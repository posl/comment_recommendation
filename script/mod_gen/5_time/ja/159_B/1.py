def is_palindrome(word):
    return word == word[::-1]
word = input()
n = len(word)

if __name__ == '__main__':
    is_palindrome()