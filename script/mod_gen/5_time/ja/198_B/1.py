def is_palindrome(string):
    return string == string[::-1]
N = input()
print("Yes" if is_palindrome(N) else "No")
