def main():
    a, b, k = map(int, input().split())
    divisors = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    print(divisors[-k])
