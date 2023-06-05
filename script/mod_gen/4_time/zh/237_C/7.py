def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
for i in range(len(s)+1):
    if is_palindrome(s + 'a'*i):
        print("Yes")
        break
else:
    print("No")

if __name__ == '__main__':
    is_palindrome()