def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True
a,b,c,d = map(int, input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print('Takahashi')
            exit()
print('Aoki')

if __name__ == '__main__':
    is_prime()