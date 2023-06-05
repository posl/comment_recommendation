def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True
T = int(input())
for i in range(T):
    N = int(input())
    for p in range(2, int(N**(1/3))+1):
        if is_prime(p):
            if N % (p**2) == 0:
                print(p, N//(p**2))
                break
