def isSquare(n):
    if int(n**0.5)**2 == n:
        return True
    else:
        return False
n = int(input())
ans = 0
for i in range(1, int(n**0.5)+1):
    if isSquare(n/i):
        ans += 1
print(ans*2)
