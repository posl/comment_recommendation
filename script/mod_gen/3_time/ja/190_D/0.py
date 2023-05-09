def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 1:
                ans += 1
    print(ans*2)

if __name__ == '__main__':
    main()