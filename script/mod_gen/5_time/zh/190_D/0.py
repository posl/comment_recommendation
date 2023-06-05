def  solve(n):
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if (i + 1) % 2 == 0 and (i + 1) // 2 > i:
                ans += 1
            if (n // i + 1) % 2 == 0 and (n // i + 1) // 2 > n // i:
                ans += 1
    return ans

if __name__ == '__main__':
    ()