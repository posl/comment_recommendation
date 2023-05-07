def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
S = input()
N = len(S)
