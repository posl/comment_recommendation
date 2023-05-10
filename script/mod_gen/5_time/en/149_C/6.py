def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1), 2):
            if n % i == 0:
                return False
        return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    is_prime()