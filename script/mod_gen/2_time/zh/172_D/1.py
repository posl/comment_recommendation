def f(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    return total
n = int(input())
total = 0
for i in range(1, n+1):
    total += i * f(i)
print(total)

if __name__ == '__main__':
    f()