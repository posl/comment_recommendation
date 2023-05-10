def check(n, x):
    while n > 0:
        if n % 2 == 1 and x % 2 == 0:
            return False
        n //= 2
        x //= 2
    return True
n = int(input())
ans = []
for i in range(n+1):
    if check(n, i):
        ans.append(i)
print(*ans, sep='\n')
