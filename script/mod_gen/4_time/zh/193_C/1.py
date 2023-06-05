def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        x = i * i
        while x <= n:
            ans -= 1
            x *= i
    print(ans)

if __name__ == '__main__':
    main()