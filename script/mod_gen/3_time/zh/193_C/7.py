def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        t = i * i
        while t <= N:
            ans -= 1
            t *= i
    print(ans)

if __name__ == '__main__':
    main()