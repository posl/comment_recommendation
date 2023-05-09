def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans = i + N // i - 2
            break
    print(ans)

if __name__ == '__main__':
    main()