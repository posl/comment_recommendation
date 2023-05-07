def sum_of_digits(n):
    return sum([int(i) for i in str(n)])
n = int(input())
print("Yes" if n % sum_of_digits(n) == 0 else "No")
