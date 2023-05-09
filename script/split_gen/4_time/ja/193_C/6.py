def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        power = i ** 2
        while power <= n:
            ans += 1
            power *= i
    print(n - ans)
