def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1,2))
a,b,c,d = map(int,input().split())
