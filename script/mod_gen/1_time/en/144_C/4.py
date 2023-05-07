def main():
    n = int(input())
    ans = 0
    if n == 2:
        ans = 1
    else:
        i = 1
        while i*i <= n:
            if n % i == 0:
                ans = i + n//i - 2
            i += 1
    print(ans)
main()

if __name__ == '__main__':
    main()