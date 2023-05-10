def fizzbuzz(n):
    if n%15 == 0:
        return "FizzBuzz"
    if n%3 == 0:
        return "Fizz"
    if n%5 == 0:
        return "Buzz"
    return str(n)
n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i if fizzbuzz(i) == str(i) else 0
print(ans)

if __name__ == '__main__':
    fizzbuzz()