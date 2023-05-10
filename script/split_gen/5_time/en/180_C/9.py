def get_divisors(n):
    divisors = []
    divisors_back = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors_back.append(n//i)
    return divisors + divisors_back[::-1]
N = int(input())
divisors = get_divisors(N)
for divisor in divisors:
    print(divisor)
