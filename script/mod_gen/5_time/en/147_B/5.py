def check_palindrome(s):
    return s == s[::-1]
s = input()
count = 0
while not check_palindrome(s):
    s = s[:-1]
    count += 1
print(count)

if __name__ == '__main__':
    check_palindrome()