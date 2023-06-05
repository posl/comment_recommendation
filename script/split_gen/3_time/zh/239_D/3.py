def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
        return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i + j == 2:
                    print("High")
                    exit()
                elif (i + j) % 2 == 0:
                    print("High")
                    exit()
                else:
                    print("Low")
                    exit()
print("Low")
