def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = "No"
for i in range(len(s)+1):
    if is_palindrome(s + "a"*i):
        ans = "Yes"
        break
print(ans)

if __name__ == '__main__':
    is_palindrome()