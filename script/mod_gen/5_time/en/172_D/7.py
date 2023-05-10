def f(x):
    counter = 0
    for i in range(1, x+1):
        if x % i == 0:
            counter += 1
    return counter
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i * f(i)
print(sum)

if __name__ == '__main__':
    f()