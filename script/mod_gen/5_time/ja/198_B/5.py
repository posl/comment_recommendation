def isPalindrome(s):
    return s == s[::-1]
N = input()
for i in range(0, 10):
    if isPalindrome('0'*i + N):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    isPalindrome()