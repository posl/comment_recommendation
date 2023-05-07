def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            if is_prime(i) and is_prime(N//i):
                print(i, N//i)
                break

if __name__ == '__main__':
    is_prime()