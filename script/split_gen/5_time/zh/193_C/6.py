def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        x = i * i
        while x <= n:
            ans -= 1
            x *= i
    print(ans)
