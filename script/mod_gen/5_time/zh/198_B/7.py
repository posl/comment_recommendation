def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] == s[-1-i]:
            continue
        else:
            return False
    else:
        return True

if __name__ == '__main__':
    isPalindrome()