def fizzbuzz(n):
    return [i if i%3 and i%5 else 'FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' for i in range(1,n+1)]
