def find_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors
n = int(input())
divisors = find_divisor(n)
divisors.sort()
for i in divisors:
    print(i)
