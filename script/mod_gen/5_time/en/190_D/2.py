def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if i % 2 == 1:
                ans += 2
            if N // i != i and (N // i) % 2 == 1:
                ans += 2
    print(ans)

if __name__ == '__main__':
    main()