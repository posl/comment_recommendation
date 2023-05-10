def main():
    N = int(input())
    ans = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans = i
        i += 1
    ans += N // ans - 2
    print(ans)

if __name__ == '__main__':
    main()