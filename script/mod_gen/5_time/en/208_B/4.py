def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
P = int(input())
count = 0
for i in range(10, 0, -1):
    count += P // factorial(i)
    P = P % factorial(i)
print(count)

if __name__ == '__main__':
    factorial()