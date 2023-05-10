def FizzBuzz(x):
    if x%3==0 and x%5==0:
        return "FizzBuzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        return str(x)
n=int(input())
s=0
for i in range(1,n+1):
    s+=int(FizzBuzz(i))
print(s)
