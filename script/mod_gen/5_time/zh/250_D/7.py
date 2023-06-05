def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
N = int(input())
p = 1
q = 1
count = 0
while p*q**3 <= N:
    if is_prime(p) and is_prime(q):
        count += 1
    if is_prime(p+1):
        p += 1
    else:
        q += 1
print(count)

if __name__ == '__main__':
    is_prime()