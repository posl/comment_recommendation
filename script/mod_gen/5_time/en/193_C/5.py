def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        num = i * i
        while num <= n:
            ans -= 1
            num *= i
    print(ans)

if __name__ == '__main__':
    main()