def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            ans = i
    print(ans + n // ans - 2)

if __name__ == '__main__':
    main()