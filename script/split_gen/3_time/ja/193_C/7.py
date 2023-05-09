def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    ans = n - 1
    for i in range(2, int(n ** 0.5) + 1):
        k = i ** 2
        while k <= n:
            ans -= 1
            k *= i
    print(ans)
