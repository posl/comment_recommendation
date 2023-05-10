def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += fizzbuzz(i)
print(ans)

if __name__ == '__main__':
    fizzbuzz()