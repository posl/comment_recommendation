def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
N = int(input())
print("Yes" if N % sum_digits(N) == 0 else "No")
