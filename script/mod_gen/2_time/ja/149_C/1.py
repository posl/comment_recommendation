def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1

if __name__ == '__main__':
    is_prime()