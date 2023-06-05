def isSquare(n):
    if n <= 0:
        return False
    else:
        m = int(n**0.5)
        if m * m == n:
            return True
        else:
            return False
n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if isSquare(i*j):
            ans += 1
print(ans)

if __name__ == '__main__':
    isSquare()