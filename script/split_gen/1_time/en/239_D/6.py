def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print("Takahashi")
            exit()
print("Aoki")
