def is_palindrome(s):
    return s == s[::-1]
S = input()
ans = 0
for i in range(len(S)):
    if S[i] != S[-(i+1)]:
        ans += 1
print(ans)

if __name__ == '__main__':
    is_palindrome()