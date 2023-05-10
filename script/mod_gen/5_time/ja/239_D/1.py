def is_prime(n):
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(b+1):
    if a <= i <= b:
        if c <= i <= d:
            if is_prime(i + i):
                print("Aoki")
                exit()
        else:
            if is_prime(i + i):
                print("Aoki")
                exit()
    else:
        break
print("Takahashi")

if __name__ == '__main__':
    is_prime()