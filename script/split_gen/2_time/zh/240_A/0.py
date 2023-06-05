def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i==0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(100):
    if prime(a + b - i):
        print('高桥')
        break
    elif prime(c + d - i):
        print('青木')
        break
