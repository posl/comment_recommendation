def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        if i ** 2 > N:
            break
        tmp = i ** 2
        while tmp <= N:
            ans -= 1
            tmp *= i
    print(ans)

if __name__ == '__main__':
    main()