def is_palindrome(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    if len(s) % 2 == 0:
        return s[0:int(len(s)/2)] == s[int(len(s)/2):][::-1]
    else:
        return s[0:int(len(s)/2)] == s[int(len(s)/2)+1:][::-1]
n = input()

if __name__ == '__main__':
    is_palindrome()