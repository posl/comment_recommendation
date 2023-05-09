def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * len([j for j in range(1, i+1) if i % j == 0])
    print(ans)

if __name__ == '__main__':
    main()