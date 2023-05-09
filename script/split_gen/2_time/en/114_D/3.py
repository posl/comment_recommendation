def main():
    N = int(input())
    divisors = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            divisors[j] += 1
    print(divisors.count(75))
