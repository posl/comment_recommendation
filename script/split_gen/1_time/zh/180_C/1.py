def get_divisors(n):
    # 約数のリストを返す
    # O(√n)
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors
n = int(input())
divisors = get_divisors(n)
for d in divisors:
    print(d)
