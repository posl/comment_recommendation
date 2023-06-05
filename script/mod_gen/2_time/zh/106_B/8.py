def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
N = int(input())
count = 0
for i in range(1, N + 1, 2):
    if len(get_divisors(i)) == 8:
        count += 1
print(count)

if __name__ == '__main__':
    get_divisors()