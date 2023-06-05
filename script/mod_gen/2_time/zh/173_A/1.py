def f(x):
    result = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            result += i
            if i != x // i:
                result += x // i
    return result
n = int(input())
result = 0
for i in range(1, n + 1):
    result += i * f(i)
print(result)

if __name__ == '__main__':
    f()