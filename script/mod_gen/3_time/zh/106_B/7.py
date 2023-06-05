def get_divisor_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
n = int(input())
count = 0
for i in range(1, n + 1, 2):
    if get_divisor_count(i) == 8:
        count += 1
print(count)

if __name__ == '__main__':
    get_divisor_count()