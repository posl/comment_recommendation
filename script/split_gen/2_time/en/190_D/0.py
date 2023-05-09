def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if (n - i * (i - 1) // 2) % i == 0:
            ans += 1
    print(ans * 2)
