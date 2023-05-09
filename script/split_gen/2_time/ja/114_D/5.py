def main():
    from math import factorial
    def prime_factorization(n):
        prime_factor = {}
        for i in range(2, n+1):
            while n % i == 0:
                if i not in prime_factor:
                    prime_factor[i] = 1
                else:
                    prime_factor[i] += 1
                n //= i
        return prime_factor
    
    N = int(input())
    if N < 75:
        print(0)
        return
    divisors = prime_factorization(factorial(N))
    divisors = list(divisors.values())
    if len(divisors) < 74:
        print(0)
        return
    divisors.sort(reverse=True)
    ans = 0
    # 75個
    for i in range(74):
        ans += divisors[i]
    # 74個
    for i in range(74):
        for j in range(i+1, 75):
            ans += divisors[i] * divisors[j]
    # 73個
    for i in range(74):
        for j in range(i+1, 75):
            for k in range(j+1, 76):
                ans += divisors[i] * divisors[j] * divisors[k]
    print(ans)
