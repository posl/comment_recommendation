def solve(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 2
            if i * i == n:
                count -= 1
    return count
n = int(input())
print(solve(n))
