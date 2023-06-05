def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False
n = int(input())
for i in range(1, n):
    if is_palindrome(str(i) + str(i)[::-1]):
        print("Yes")
        exit()
print("No")
