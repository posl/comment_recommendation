def divisors(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += 1
    return count
N = int(input())
count = 0
for i in range(1, N + 1):
    if divisors(i) == 8:
        count += 1
print(count)

if __name__ == '__main__':
    divisors()