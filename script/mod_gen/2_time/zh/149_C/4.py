def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1

if __name__ == '__main__':
    is_prime()