def is_palindrome(s):
    return s == s[::-1]
S = input()
ans = "Yes" if is_palindrome(S) else "No"
print(ans)

if __name__ == '__main__':
    is_palindrome()