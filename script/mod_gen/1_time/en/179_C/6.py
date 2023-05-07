def sum_divisors(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans += i
            if i != n // i:
                ans += n // i
    return ans
N = int(input())
print(sum_divisors(N) - N)

if __name__ == '__main__':
    sum_divisors()