def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        t = i * i
        while t <= n:
            ans -= 1
            t *= i
    print(ans)

if __name__ == '__main__':
    main()