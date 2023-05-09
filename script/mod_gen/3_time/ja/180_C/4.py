def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return sorted(divisors)
N = int(input())
ans = divisors(N)
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    divisors()