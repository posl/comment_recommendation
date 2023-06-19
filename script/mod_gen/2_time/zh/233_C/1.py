def get_divisor(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return divisors
n, x = map(int, input().split())
bags = []
for i in range(n):
    bags.append(list(map(int, input().split())))
divisors = get_divisor(x)
ans = 0
for divisor in divisors:
    for bag in bags:
        for ball in bag[1:]:
            if ball == divisor:
                ans += 1
                break
print(ans)

if __name__ == '__main__':
    get_divisor()