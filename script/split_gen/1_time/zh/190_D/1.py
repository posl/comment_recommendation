def main():
    n = int(input())
    ans = 0
    for i in range(1, int((2 * n) ** 0.5) + 1):
        if 2 * n % i == 0:
            m = 2 * n // i
            if (i - m + 1) % 2 == 0:
                if (i - m + 1) // 2 > 0:
                    ans += 1
            if (m - i + 1) % 2 == 0:
                if (m - i + 1) // 2 > 0:
                    ans += 1
    print(ans)
