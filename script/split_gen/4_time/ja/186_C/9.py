def num_of_7(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == '7':
            return 1
    return 0
n = int(input())
ans = 0
for i in range(1, n+1):
    if num_of_7(i) == 0 and num_of_7(int(oct(i)[2:])) == 0:
        ans += 1
print(ans)
