def main():
    N = int(input())
    ans = 0
    for i in range(2, 1000000):
        if N % i == 0:
            ans += 1
            N = N // i
            while N % i == 0:
                N = N // i
    if N != 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()