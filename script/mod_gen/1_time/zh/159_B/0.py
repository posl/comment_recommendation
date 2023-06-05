def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:
            return False
    return True
s=input()
n=len(s)

if __name__ == '__main__':
    is_palindrome()