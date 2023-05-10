def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2): # 3~nの平方根まで2刻みで繰り返し
        if n % i == 0:
            return False
    return True
X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1
