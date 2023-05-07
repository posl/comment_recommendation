def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if not num % i:
            return False
    return True
x = int(input())
while not is_prime(x):
    x += 1
print(x)

if __name__ == '__main__':
    is_prime()