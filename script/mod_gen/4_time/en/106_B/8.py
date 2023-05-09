def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True
n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1:
        if is_prime(i):
            count += 1
        if count == 8:
            print(i)
            break

if __name__ == '__main__':
    is_prime()