def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if i % 2 == 0 and j % 2 == 1:
                ans += 1
            if i % 2 == 1 and j % 2 == 0:
                ans += 1
    print(ans)
