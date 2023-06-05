def f(x):
    sum = 0
    for i in range(1,x+1):
        if x % i == 0:
            sum += 1
    return sum
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i * f(i)
print(sum)

if __name__ == '__main__':
    f()