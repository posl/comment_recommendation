def isPalindromic(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    isPalindromic()