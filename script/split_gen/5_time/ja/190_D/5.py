def solve(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 1:
                cnt += 2
            if i**2 == n:
                cnt -= 1
    return cnt
n = int(input())
print(solve(n))
