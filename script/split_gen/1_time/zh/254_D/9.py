def isSquare(n):
    if n < 0:
        return False
    else:
        return (n**0.5).is_integer()
    
N = int(input())
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if isSquare(i*j):
            ans += 1
print(ans)
