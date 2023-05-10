def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True
A,B,C,D = map(int,input().split())

if __name__ == '__main__':
    is_prime()