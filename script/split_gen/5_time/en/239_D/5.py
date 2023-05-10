def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
A,B,C,D = map(int, input().split())
for i in range(100):
    if is_prime(A+i) and is_prime(D+i):
        print("Prime")
        exit()
print("Not Prime")
