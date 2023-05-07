def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)

if __name__ == '__main__':
    is_prime()