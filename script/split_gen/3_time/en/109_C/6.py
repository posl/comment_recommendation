def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(x)
nums.sort()
diff = [nums[i+1] - nums[i] for i in range(n)]
ans = diff[0]
for i in range(1, n):
    ans = gcd(ans, diff[i])
print(ans)
