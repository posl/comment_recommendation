def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if (N - i) % i == 0:
            ans += 1
        if (N - i) % (i + 1) == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()