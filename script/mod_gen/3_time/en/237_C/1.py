def isPalindrome(s):
    return s == s[::-1]
s = input()
for i in range(len(s)+1):
    if isPalindrome('a'*i+s):
        print('Yes')
        break
else:
    print('No')

if __name__ == '__main__':
    isPalindrome()