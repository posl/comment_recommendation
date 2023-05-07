def divisor(x):
    i = 1
    result = 0
    while i*i <= x:
        if x%i == 0:
            result += 1
            if x//i != i:
                result += 1
        i += 1
    return result
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*divisor(i)
print(ans)
