def solve():
    n = int(input())
    ans = 0
    for i in range(2, int(n**0.25)+1):
        if n % i == 0:
            n2 = n // i
            for j in range(2, int(n2**0.33)+1):
                if n2 % j == 0:
                    ans += 1
    print(ans)
