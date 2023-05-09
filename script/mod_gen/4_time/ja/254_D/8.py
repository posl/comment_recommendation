def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    if n % 2 == 1:
        return False
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True
n = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if is_square(i*j):
            ans += 1
print(ans)

if __name__ == '__main__':
    is_square()