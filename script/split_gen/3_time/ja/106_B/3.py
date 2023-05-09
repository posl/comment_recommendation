def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
N = int(input())
count = 0
for i in range(1, N+1, 2):
    if is_prime(i):
        continue
    elif i % 2 == 0:
        continue
    else:
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 8:
            count = 0
        else:
            count = 0
            continue
        print(i)
        count = 0
