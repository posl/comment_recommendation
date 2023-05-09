def main():
    N = int(input())
    print(sum(K*divisors(K) for K in range(1, N+1)))
