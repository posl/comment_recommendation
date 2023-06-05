def FizzBuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += FizzBuzz(i)
print(sum)

if __name__ == '__main__':
    FizzBuzz()