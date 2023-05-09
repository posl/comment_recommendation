def isPalindrome(n):
    n = str(n)
    if n == n[::-1]: return True
    else: return False
N = int(input())

if __name__ == '__main__':
    isPalindrome()