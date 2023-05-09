def f(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count
N = int(input())
result = 0
for i in range(1,N+1):
    result += i * f(i)
print(result)

if __name__ == '__main__':
    f()