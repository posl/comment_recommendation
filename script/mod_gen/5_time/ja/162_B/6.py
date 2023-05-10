def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += fizzbuzz(i)
print(ans)

if __name__ == '__main__':
    fizzbuzz()