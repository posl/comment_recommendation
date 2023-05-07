def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(1, M + 1):
        if M % i == 0 and i <= M // N:
            ans = i
    print(ans)

if __name__ == '__main__':
    main()