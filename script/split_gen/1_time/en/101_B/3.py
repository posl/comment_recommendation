def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
n = int(input())
print("Yes" if n % digit_sum(n) == 0 else "No")
