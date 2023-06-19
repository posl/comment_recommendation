def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        else:
            return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                print('Y')
                break
        else:
            print('N')
        break
else:
    print('N')

if __name__ == '__main__':
    is_prime()