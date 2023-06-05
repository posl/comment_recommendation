def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
count = 0
for i in range(len(s)):
    if is_palindrome(s[i:]):
        print("Yes")
        exit()
print("No")

if __name__ == '__main__':
    is_palindrome()