def is_square(n):
    sqrt_n = int(n**0.5)
    return sqrt_n*sqrt_n == n
n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if is_square(i*j):
            ans += 1
print(ans)

if __name__ == '__main__':
    is_square()