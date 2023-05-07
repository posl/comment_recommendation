def is_prime(x):
    if x < 2: return False
    if x == 2: return True
    if x%2 == 0: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True
a,b,c,d = map(int, input().split())
for i in range(100):
    if a+i > b:
        print('Aoki')
        exit()
    if c+i > d:
        print('Takahashi')
        exit()
    if is_prime(a+i+c+i):
        print('Aoki')
        exit()
    if is_prime(a+i+c+i+1):
        print('Takahashi')
        exit()

if __name__ == '__main__':
    is_prime()