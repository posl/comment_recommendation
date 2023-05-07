def sum_of_digits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum
n = int(input())
print("Yes" if n % sum_of_digits(n) == 0 else "No")

if __name__ == '__main__':
    sum_of_digits()