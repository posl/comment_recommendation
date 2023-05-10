def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += fizzbuzz(i)
print(sum)

if __name__ == '__main__':
    fizzbuzz()