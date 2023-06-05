def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True
n = int(input())
while not is_prime(n):
    n += 1
print(n)

if __name__ == '__main__':
    is_prime()