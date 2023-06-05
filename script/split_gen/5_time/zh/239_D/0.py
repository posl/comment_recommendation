def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print('高桥')
            exit()
print('青木')
