def main():
    N = int(input())
    ans = 0
    # Nが素数の場合
    if N % 2 != 0 and N % 3 != 0:
        print(1)
        return
    # Nが2の累乗の場合
    while N % 2 == 0:
        N //= 2
        ans += 1
    # Nが3の累乗の場合
    while N % 3 == 0:
        N //= 3
        ans += 1
    # Nが2の累乗でない場合
    i = 5
    while i ** 2 <= N:
        while N % i == 0:
            N //= i
            ans += 1
        i += 2
    # Nが3の累乗でない場合
    i = 7
    while i ** 2 <= N:
        while N % i == 0:
            N //= i
            ans += 1
        i += 2
    # Nが素数の場合
    if N != 1:
        print(ans + 1)
    else:
        print(ans)

if __name__ == '__main__':
    main()