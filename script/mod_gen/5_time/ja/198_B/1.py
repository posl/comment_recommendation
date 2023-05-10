def is_palindrome(string):
    return string == string[::-1]
N = input()
print("Yes" if is_palindrome(N) else "No")

if __name__ == '__main__':
    is_palindrome()