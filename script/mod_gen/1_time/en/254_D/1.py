def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j <= N:
                ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()