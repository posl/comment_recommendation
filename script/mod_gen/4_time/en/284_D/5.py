def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            if is_prime(n // j):
                print(str(j) + " " + str(n // j))
                break

if __name__ == '__main__':
    is_prime()