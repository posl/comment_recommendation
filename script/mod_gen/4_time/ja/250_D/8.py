def main():
    n = int(input())
    ans = 0
    for i in range(1, 100000):
        if i >= n:
            break
        if i % 2 == 0:
            continue
        if n % i == 0:
            tmp = n // i
            if tmp % 2 == 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()