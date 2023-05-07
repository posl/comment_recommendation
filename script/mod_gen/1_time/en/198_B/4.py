def palindrome(n):
    if n == n[::-1]:
        return 'Yes'
    else:
        return 'No'
n = input()
print(palindrome(n))

if __name__ == '__main__':
    palindrome()