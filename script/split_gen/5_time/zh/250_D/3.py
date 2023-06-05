def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    else:
        i = 3
        while i*i <= n:
            if n%i == 0:
                return False
            i += 2
        return True
N = int(input())
count = 0
for q in range(1,int(N**(1/3))+1):
    if is_prime(q):
        for p in range(1,q):
            if is_prime(p):
                if p*q**3 <= N:
                    count += 1
                else:
                    break
print(count)
